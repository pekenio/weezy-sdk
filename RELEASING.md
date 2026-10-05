# Publishing releases

The repository contains both SDKs. Version numbers are in `typescript/package.json`, `python/pyproject.toml`, and `python/src/weezy/__init__.py`. Run `npm install --package-lock-only` in `typescript` when changing its version.

## npm

The first publication can be made locally from `typescript` with `npm publish --access public` after `npm login` and passing tests. Complete the requested browser/2FA challenge.

For subsequent releases, configure an npm Trusted Publisher for `@weezy/sdk` using this GitHub repository and workflow filename `publish.yml`, with publish permission. The workflow runs on GitHub-hosted runners and uses OIDC without a stored npm token.

## PyPI

Version 0.1.0 is published at https://pypi.org/project/weezy-sdk/. GitHub Trusted Publishing is configured with these values:

- PyPI project: `weezy-sdk`
- GitHub owner: `pekenio`
- GitHub repository: `weezy-sdk`
- Workflow filename: `publish.yml`
- Environment: `pypi`

For an existing project, configure the same values under its Publishing settings. The account needs ownership of the project name. No PyPI token is needed for this workflow.

Run the **Publish SDKs** workflow manually from GitHub Actions, choosing npm and/or PyPI. The workflows run tests and build before publishing. Use `main` for releases. Versions cannot be reused for different archives; bump versions before subsequent releases.

Create a GitHub release with a version tag after successful publication. Do not include credentials, local environment files, dependencies or built distributions in Git commits.
