import { operations, type SmsAPI } from "./resources.js";
export type * from "./resources.js";
export type * from "./types.js";

export class WeezyError extends Error {
  constructor(message: string, public readonly status: number, public readonly details: unknown,
    public readonly requestId: string | null = null) { super(message); this.name = "WeezyError"; }
}
export interface WeezyOptions {
  clientId: string; clientSecret: string; baseUrl?: string; timeoutMs?: number;
  /** Replace fetch for tests or custom server transports. */
  fetch?: typeof globalThis.fetch;
}
type Operation = { method: string; path: string; body: boolean; unwrap: boolean; params: readonly { name: string; in: string }[] };
export class Weezy {
  readonly sms: SmsAPI;
  readonly #baseUrl: string;
  readonly #authorization: string;
  readonly #timeout: number;
  readonly #fetcher: typeof globalThis.fetch;
  constructor(options: WeezyOptions) {
    if (!options.clientId || !options.clientSecret || options.clientId.includes(":")) throw new TypeError("Valid clientId and clientSecret are required");
    const url = new URL(options.baseUrl ?? "https://api.weezy.app/client/api/v1");
    if (!["http:", "https:"].includes(url.protocol) || url.username || url.password || url.search || url.hash) throw new TypeError("Invalid baseUrl");
    this.#baseUrl = url.toString().replace(/\/$/, "");
    this.#authorization = "Basic " + Buffer.from(options.clientId + ":" + options.clientSecret).toString("base64");
    this.#timeout = options.timeoutMs ?? 30000;
    if (!Number.isFinite(this.#timeout) || this.#timeout <= 0) throw new TypeError("timeoutMs must be positive");
    this.#fetcher = options.fetch ?? globalThis.fetch;
    this.sms = this.resource(operations.sms) as unknown as SmsAPI;
  }
  private segment(value: unknown): string {
    if (value === undefined || value === null || String(value) === "" || [".", ".."].includes(String(value))) throw new TypeError("A valid path parameter is required");
    return encodeURIComponent(String(value));
  }
  private resource(methods: Record<string, Operation>) {
    return Object.fromEntries(Object.entries(methods).map(([name, op]) => [name, async (...args: unknown[]) => {
      const params = (args[op.body ? 1 : 0] ?? {}) as Record<string, unknown>;
      const query = new URLSearchParams();
      let path = op.path;
      for (const param of op.params) {
        const value = params[param.name];
        if (param.in === "path") path = path.replace(`{${param.name}}`, this.segment(value));
        else if (value !== undefined && value !== null) {
          for (const item of Array.isArray(value) ? value : [value]) query.append(param.name, String(item));
        }
      }
      if (op.body && args[0] === undefined) throw new TypeError("A request body is required");
      return this.request(op.method, path + (query.size ? "?" + query : ""), op.body ? args[0] : undefined, op.unwrap);
    }]));
  }
  private async request(method: string, path: string, body: unknown, unwrap: boolean): Promise<unknown> {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), this.#timeout);
    try {
      const response = await this.#fetcher(this.#baseUrl + path, {
        method, headers: { Authorization: this.#authorization, Accept: "application/json", ...(body === undefined ? {} : { "Content-Type": "application/json" }) },
        body: body === undefined ? undefined : JSON.stringify(body), signal: controller.signal, redirect: "error",
      });
      const text = await response.text();
      let data: unknown;
      try { data = text ? JSON.parse(text) : null; }
      catch { throw new WeezyError("API returned a non-JSON response", response.status, text, response.headers.get("x-request-id")); }
      const envelope = data as { code?: number; msg?: string; detail?: unknown; data?: unknown } | null;
      if (!response.ok || (unwrap && typeof envelope?.code === "number" && envelope.code >= 400)) {
        throw new WeezyError(envelope?.msg ?? (typeof envelope?.detail === "string" ? envelope.detail : `API request failed (${response.status})`), response.status, data, response.headers.get("x-request-id"));
      }
      return unwrap && envelope && typeof envelope.code === "number" && "msg" in envelope ? envelope.data : data;
    } catch (error) {
      if (error instanceof WeezyError) throw error;
      throw new WeezyError(controller.signal.aborted ? "Request timed out" : "Network request failed", 0, null);
    } finally { clearTimeout(timer); }
  }
}
