// Generated.
import type * as T from "./types.js";
export interface BroadcastsAPI {
  /** All broadcast lists */
  allBroadcasts(): Promise<Array<T.SimpleOut>>;
}
export interface ChatsAPI {
  /** All chats */
  allChats(): Promise<Array<T.SimpleOut>>;
  /** List chats */
  listChats(): Promise<Array<T.SimpleOut>>;
  /** Unread messages */
  unreadMessages(): Promise<Array<T.SimpleOut>>;
  /** Typing state */
  typing(body: T.ChatPhoneBoolIn): Promise<T.ActionResultOut>;
  /** Send seen */
  sendSeen(body: T.ChatPhoneIn): Promise<T.ActionResultOut>;
  /** All archived chats */
  allChatsArchived(): Promise<Array<T.SimpleOut>>;
  /** All chats with messages */
  allChatsWithMessages(): Promise<Array<T.SimpleOut>>;
  /** Chat by id */
  chatById(params: { phone: string }): Promise<T.SimpleOut>;
  /** Chat is online */
  chatIsOnline(params: { phone: string }): Promise<T.SimpleOut>;
  /** Last seen */
  lastSeen(params: { phone: string }): Promise<T.SimpleOut>;
  /** List mutes */
  listMutes(params: { mute_type: string }): Promise<Array<T.SimpleOut>>;
  /** Load messages in chat */
  loadMessagesInChat(body: T.LoadMessagesInChatIn): Promise<Array<T.SimpleOut>>;
  /** Get messages */
  getMessages(params: { phone: string }): Promise<Array<T.SimpleOut>>;
  /** All new messages */
  allNewMessages(): Promise<Array<T.SimpleOut>>;
  /** All unread messages */
  allUnreadMessages(): Promise<Array<T.SimpleOut>>;
  /** Load messages in chat (GET) */
  loadMessagesGet(params: { phone: string; count?: number }): Promise<Array<T.SimpleOut>>;
  /** Get message by id */
  messageById(params: { message_id: string }): Promise<T.SimpleOut>;
  /** Archive chat */
  archiveChat(body: T.ChatPhoneBoolIn): Promise<T.ActionResultOut>;
  /** Archive all chats */
  archiveAllChats(): Promise<T.ActionResultOut>;
  /** Clear chat */
  clearChat(body: T.ChatPhoneIn): Promise<T.ActionResultOut>;
  /** Clear all chats */
  clearAllChats(): Promise<T.ActionResultOut>;
  /** Delete chat */
  deleteChat(body: T.ChatPhoneIn): Promise<T.ActionResultOut>;
  /** Delete all chats */
  deleteAllChats(): Promise<T.ActionResultOut>;
  /** Delete message */
  deleteMessage(body: T.MessageIdIn): Promise<T.ActionResultOut>;
  /** Mark unseen */
  markUnseen(body: T.ChatPhoneIn): Promise<T.ActionResultOut>;
  /** Pin chat */
  pinChat(body: T.ChatPhoneBoolIn): Promise<T.ActionResultOut>;
  /** Set chat state */
  chatState(body: T.ChatStateIn): Promise<T.ActionResultOut>;
  /** Recording state */
  chatRecording(body: T.ChatPhoneBoolIn): Promise<T.ActionResultOut>;
  /** Set temporary messages */
  temporaryMessages(body: T.TemporaryMessagesIn): Promise<T.ActionResultOut>;
  /** Star a message */
  starMessage(body: T.StarMessageIn): Promise<T.ActionResultOut>;
  /** Get reactions for message */
  reactions(params: { message_id: string }): Promise<Array<T.SimpleOut>>;
  /** Get votes for message */
  votes(params: { message_id: string }): Promise<Array<T.SimpleOut>>;
  /** Reject call */
  rejectCall(body: T.ChatPhoneIn): Promise<T.ActionResultOut>;
  /** Send mute */
  sendMute(body: T.SendMuteIn): Promise<T.ActionResultOut>;
}
export interface CommunityAPI {
  /** Create community */
  createCommunity(body: T.CreateCommunityIn): Promise<T.ActionResultOut>;
  /** Deactivate community */
  deactivateCommunity(body: T.CommunityIdIn): Promise<T.ActionResultOut>;
  /** Add subgroups to community */
  addSubgroup(body: T.CommunitySubgroupsIn): Promise<T.ActionResultOut>;
  /** Remove subgroups from community */
  removeSubgroup(body: T.CommunitySubgroupsIn): Promise<T.ActionResultOut>;
  /** Promote community participants */
  promoteParticipant(body: T.CommunityParticipantsIn): Promise<T.ActionResultOut>;
  /** Demote community participants */
  demoteParticipant(body: T.CommunityParticipantsIn): Promise<T.ActionResultOut>;
  /** List community participants */
  communityParticipants(params: { id: string }): Promise<Array<T.SimpleOut>>;
}
export interface ContactsAPI {
  /** All contacts */
  allContacts(): Promise<Array<T.ContactOut>>;
  /** Check number status */
  checkNumberStatus(params: { phone: string }): Promise<T.CheckNumberStatusOut>;
  /** Get contact by phone */
  getContact(params: { phone: string }): Promise<T.ContactOut>;
  /** Get profile */
  profile(params: { phone: string }): Promise<T.ProfileOut>;
  /** Get profile picture */
  profilePic(params: { phone: string }): Promise<T.ProfilePicOut>;
  /** Get profile status */
  profileStatus(params: { phone: string }): Promise<T.ProfileOut>;
  /** Get block list */
  blocklist(): Promise<Array<string>>;
  /** Block contact */
  blockContact(params: { phone: string }): Promise<T.ActionResultOut>;
  /** Unblock contact */
  unblockContact(params: { phone: string }): Promise<T.ActionResultOut>;
  /** Send contact vCard */
  contactVcard(body: T.ChatPhoneIn): Promise<T.ActionResultOut>;
  /** Get battery level */
  getBatteryLevel(): Promise<{ [key: string]: unknown }>;
}
export interface GroupsAPI {
  /** List groups */
  listGroups(): Promise<Array<T.SimpleOut>>;
  /** List group members */
  listGroupMembers(params: { group_id: string }): Promise<Array<T.SimpleOut>>;
  /** Common groups with wid */
  commonGroups(params: { wid: string }): Promise<Array<T.SimpleOut>>;
  /** Group admins */
  groupAdmins(params: { group_id: string }): Promise<Array<T.SimpleOut>>;
  /** Invite link */
  groupInviteLink(params: { group_id: string }): Promise<T.SimpleOut>;
  /** Revoke invite link */
  groupRevokeLink(params: { group_id: string }): Promise<T.ActionResultOut>;
  /** Group member IDs */
  groupMemberIds(params: { group_id: string }): Promise<Array<string>>;
  /** Create group */
  createGroup(body: T.CreateGroupIn): Promise<T.ActionResultOut>;
  /** Leave group */
  leaveGroup(body: T.LeaveGroupIn): Promise<T.ActionResultOut>;
  /** Get join code */
  joinCode(params: { group_id: string }): Promise<T.SimpleOut>;
  /** Add participants */
  addParticipants(body: T.ParticipantsIn): Promise<T.ActionResultOut>;
  /** Remove participants */
  removeParticipants(body: T.ParticipantsIn): Promise<T.ActionResultOut>;
  /** Promote participants */
  promoteParticipants(body: T.ParticipantsIn): Promise<T.ActionResultOut>;
  /** Demote participants */
  demoteParticipants(body: T.ParticipantsIn): Promise<T.ActionResultOut>;
  /** Group info from invite link */
  groupInfoFromInviteLink(params: { invite_code: string }): Promise<T.SimpleOut>;
  /** Set group description */
  groupDescription(body: T.GroupDescriptionIn): Promise<T.ActionResultOut>;
  /** Set group property */
  groupProperty(body: T.GroupPropertyIn): Promise<T.ActionResultOut>;
  /** Set group subject */
  groupSubject(body: T.GroupSubjectIn): Promise<T.ActionResultOut>;
  /** Toggle messages only for admins */
  messagesAdminsOnly(body: T.MessagesAdminsOnlyIn): Promise<T.ActionResultOut>;
  /** Set group picture */
  groupPicture(body: T.GroupPicIn): Promise<T.ActionResultOut>;
  /** Change privacy of group */
  changePrivacyGroup(body: T.ChangePrivacyGroupIn): Promise<T.ActionResultOut>;
}
export interface LabelsAPI {
  /** Get all labels */
  getAllLabels(): Promise<Array<T.SimpleOut>>;
  /** Add new label */
  addLabel(body: T.AddLabelIn): Promise<T.ActionResultOut>;
  /** Add or remove label on chats */
  addOrRemoveLabel(body: T.AddOrRemoveLabelIn): Promise<T.ActionResultOut>;
  /** Delete all labels */
  deleteAllLabels(): Promise<T.ActionResultOut>;
  /** Delete label by id */
  deleteLabel(params: { label_id: string }): Promise<T.ActionResultOut>;
}
export interface MediaAPI {
  /** Get platform from message */
  platformFromMessage(params: { message_id: string }): Promise<T.SimpleOut>;
  /** Download media by message */
  downloadMedia(params: { messageId: string }): Promise<T.SimpleOut>;
}
export interface MessagesAPI {
  /** Send text message */
  sendTextMessage(body: T.MessageTextIn): Promise<T.ActionResultOut>;
  /** Send image (base64) */
  sendImageMessage(body: T.MessageImageIn): Promise<T.ActionResultOut>;
  /** Send link preview */
  sendLinkPreview(body: T.LinkPreviewIn): Promise<T.ActionResultOut>;
  /** Send location */
  sendLocation(body: T.LocationIn): Promise<T.ActionResultOut>;
  /** Send file base64 */
  sendFileBase64(body: T.FileBase64In): Promise<T.ActionResultOut>;
  /** Send voice base64 */
  sendVoiceBase64(body: T.VoiceBase64In): Promise<T.ActionResultOut>;
  /** Get media by message id */
  getMediaByMessage(params: { message_id: string }): Promise<T.SimpleOut>;
  /** Edit a message */
  editMessage(body: T.EditMessageIn): Promise<T.ActionResultOut>;
  /** Forward messages */
  forwardMessages(body: T.ForwardMessagesIn): Promise<T.ActionResultOut>;
  /** React to a message */
  reactMessage(body: T.ReactMessageIn): Promise<T.ActionResultOut>;
  /** Send reply message */
  sendReply(body: T.ReplyMessageIn): Promise<T.ActionResultOut>;
  /** Send sticker (base64) */
  sendSticker(body: T.StickerIn): Promise<T.ActionResultOut>;
  /** Send mentioned message */
  sendMentioned(body: T.MentionedIn): Promise<T.ActionResultOut>;
  /** Send buttons message */
  sendButtons(body: T.ButtonsIn): Promise<T.ActionResultOut>;
  /** Send list message */
  sendListMessage(body: T.ListMessageIn): Promise<T.ActionResultOut>;
  /** Send order message */
  sendOrderMessage(body: T.OrderMessageIn): Promise<T.ActionResultOut>;
  /** Send poll message */
  sendPollMessage(body: T.PollMessageIn): Promise<T.ActionResultOut>;
  /** Send profile status text */
  sendStatusText(body: T.SendStatusIn): Promise<T.ActionResultOut>;
}
export interface MiscAPI {
  /** Get current account phone number */
  getPhoneNumber(): Promise<T.SimpleOut>;
}
export interface PresenceAPI {
  /** Subscribe presence */
  subscribePresence(body: T.ChatPhoneIn): Promise<T.ActionResultOut>;
  /** Set online presence */
  setOnlinePresence(body: T.ChatPhoneBoolIn): Promise<T.ActionResultOut>;
}
export interface ProductsAPI {
  /** Get products */
  getProducts(): Promise<Array<T.SimpleOut>>;
  /** Add product */
  addProduct(body: T.AddProductIn): Promise<T.ActionResultOut>;
  /** Get product by id */
  getProductById(params: { product_id: string }): Promise<T.SimpleOut>;
  /** Edit product */
  editProduct(body: T.EditProductIn): Promise<T.ActionResultOut>;
  /** Delete products */
  deleteProducts(body: T.DeleteProductsIn): Promise<T.ActionResultOut>;
  /** Change product image */
  changeProductImage(body: T.ProductImageIn): Promise<T.ActionResultOut>;
  /** Add product image */
  addProductImage(body: T.ProductImageIn): Promise<T.ActionResultOut>;
  /** Remove product image */
  removeProductImage(body: T.ProductImageIn): Promise<T.ActionResultOut>;
  /** Set product visibility */
  setProductVisibility(body: T.ProductVisibilityIn): Promise<T.ActionResultOut>;
  /** Enable/disable cart */
  setCartEnabled(body: T.SetCartEnabledIn): Promise<T.ActionResultOut>;
  /** Get collections */
  getCollections(): Promise<Array<T.SimpleOut>>;
  /** Create collection */
  createCollection(body: T.CreateCollectionIn): Promise<T.ActionResultOut>;
  /** Edit collection */
  editCollection(body: T.EditCollectionIn): Promise<T.ActionResultOut>;
  /** Delete collection */
  deleteCollection(body: T.DeleteCollectionIn): Promise<T.ActionResultOut>;
  /** Send link catalog */
  sendLinkCatalog(): Promise<T.ActionResultOut>;
}
export interface SmsAPI {
  /** Remaining wallet balance */
  balance(): Promise<T.WalletOut>;
  /** Sender IDs available for sending */
  senders(): Promise<{ [key: string]: unknown }>;
  /** Send one SMS */
  send(body: T.SmsSendIn): Promise<T.SmsMessageOut>;
  /** Send the same SMS to many recipients */
  sendBulk(body: T.SmsBulkSendIn): Promise<T.SmsBulkSendOut>;
  /** Get the delivery status of one SMS */
  status(params: { message_x_id: string }): Promise<T.SmsMessageOut>;
  /** Unsubscribe numbers (excluded from all future sends) */
  optOuts(body: T.SmsOptOutIn): Promise<{ [key: string]: unknown }>;
}
export interface StoriesAPI {
  /** Send text storie */
  sendTextStorie(body: T.MessageTextIn): Promise<T.ActionResultOut>;
  /** Send image storie (base64) */
  sendImageStorie(body: T.MessageImageIn): Promise<T.ActionResultOut>;
  /** Send video storie (base64) */
  sendVideoStorie(body: T.MessageImageIn): Promise<T.ActionResultOut>;
}
export interface WhatsAppAPI {
  broadcasts: BroadcastsAPI;
  chats: ChatsAPI;
  community: CommunityAPI;
  contacts: ContactsAPI;
  groups: GroupsAPI;
  labels: LabelsAPI;
  media: MediaAPI;
  messages: MessagesAPI;
  misc: MiscAPI;
  presence: PresenceAPI;
  products: ProductsAPI;
  stories: StoriesAPI;
}
export const operations = {
  "broadcasts": {
    "allBroadcasts": {
      "method": "GET",
      "path": "/{instance_id}/broadcasts",
      "body": false,
      "params": [],
      "unwrap": false
    }
  },
  "chats": {
    "allChats": {
      "method": "GET",
      "path": "/{instance_id}/chats",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "listChats": {
      "method": "GET",
      "path": "/{instance_id}/chats/list",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "unreadMessages": {
      "method": "GET",
      "path": "/{instance_id}/chats/unread",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "typing": {
      "method": "POST",
      "path": "/{instance_id}/chats/typing",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendSeen": {
      "method": "POST",
      "path": "/{instance_id}/chats/send-seen",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "allChatsArchived": {
      "method": "GET",
      "path": "/{instance_id}/chats/archived",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "allChatsWithMessages": {
      "method": "GET",
      "path": "/{instance_id}/chats/with-messages",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "chatById": {
      "method": "GET",
      "path": "/{instance_id}/chats/by-id/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "chatIsOnline": {
      "method": "GET",
      "path": "/{instance_id}/chats/is-online/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "lastSeen": {
      "method": "GET",
      "path": "/{instance_id}/chats/last-seen/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "listMutes": {
      "method": "GET",
      "path": "/{instance_id}/chats/list-mutes/{mute_type}",
      "body": false,
      "params": [
        {
          "name": "mute_type",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "loadMessagesInChat": {
      "method": "POST",
      "path": "/{instance_id}/chats/load-messages",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "getMessages": {
      "method": "GET",
      "path": "/{instance_id}/chats/messages/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "allNewMessages": {
      "method": "GET",
      "path": "/{instance_id}/chats/new",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "allUnreadMessages": {
      "method": "GET",
      "path": "/{instance_id}/chats/all-unread",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "loadMessagesGet": {
      "method": "GET",
      "path": "/{instance_id}/chats/load-messages/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        },
        {
          "name": "count",
          "in": "query"
        }
      ],
      "unwrap": false
    },
    "messageById": {
      "method": "GET",
      "path": "/{instance_id}/chats/message-by-id/{message_id}",
      "body": false,
      "params": [
        {
          "name": "message_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "archiveChat": {
      "method": "POST",
      "path": "/{instance_id}/chats/archive",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "archiveAllChats": {
      "method": "POST",
      "path": "/{instance_id}/chats/archive-all",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "clearChat": {
      "method": "POST",
      "path": "/{instance_id}/chats/clear",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "clearAllChats": {
      "method": "POST",
      "path": "/{instance_id}/chats/clear-all",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "deleteChat": {
      "method": "POST",
      "path": "/{instance_id}/chats/delete",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "deleteAllChats": {
      "method": "POST",
      "path": "/{instance_id}/chats/delete-all",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "deleteMessage": {
      "method": "POST",
      "path": "/{instance_id}/chats/delete-message",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "markUnseen": {
      "method": "POST",
      "path": "/{instance_id}/chats/mark-unseen",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "pinChat": {
      "method": "POST",
      "path": "/{instance_id}/chats/pin",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "chatState": {
      "method": "POST",
      "path": "/{instance_id}/chats/chat-state",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "chatRecording": {
      "method": "POST",
      "path": "/{instance_id}/chats/recording",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "temporaryMessages": {
      "method": "POST",
      "path": "/{instance_id}/chats/temporary-messages",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "starMessage": {
      "method": "POST",
      "path": "/{instance_id}/chats/star-message",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "reactions": {
      "method": "GET",
      "path": "/{instance_id}/chats/reactions/{message_id}",
      "body": false,
      "params": [
        {
          "name": "message_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "votes": {
      "method": "GET",
      "path": "/{instance_id}/chats/votes/{message_id}",
      "body": false,
      "params": [
        {
          "name": "message_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "rejectCall": {
      "method": "POST",
      "path": "/{instance_id}/chats/reject-call",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendMute": {
      "method": "POST",
      "path": "/{instance_id}/chats/send-mute",
      "body": true,
      "params": [],
      "unwrap": false
    }
  },
  "community": {
    "createCommunity": {
      "method": "POST",
      "path": "/{instance_id}/community/create",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "deactivateCommunity": {
      "method": "POST",
      "path": "/{instance_id}/community/deactivate",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "addSubgroup": {
      "method": "POST",
      "path": "/{instance_id}/community/add-subgroup",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "removeSubgroup": {
      "method": "POST",
      "path": "/{instance_id}/community/remove-subgroup",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "promoteParticipant": {
      "method": "POST",
      "path": "/{instance_id}/community/promote-participant",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "demoteParticipant": {
      "method": "POST",
      "path": "/{instance_id}/community/demote-participant",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "communityParticipants": {
      "method": "GET",
      "path": "/{instance_id}/community/participants/{id}",
      "body": false,
      "params": [
        {
          "name": "id",
          "in": "path"
        }
      ],
      "unwrap": false
    }
  },
  "contacts": {
    "allContacts": {
      "method": "GET",
      "path": "/{instance_id}/contacts",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "checkNumberStatus": {
      "method": "GET",
      "path": "/{instance_id}/contacts/check-number-status/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "getContact": {
      "method": "GET",
      "path": "/{instance_id}/contacts/contact/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "profile": {
      "method": "GET",
      "path": "/{instance_id}/contacts/profile/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "profilePic": {
      "method": "GET",
      "path": "/{instance_id}/contacts/profile-pic/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "profileStatus": {
      "method": "GET",
      "path": "/{instance_id}/contacts/profile-status/{phone}",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "blocklist": {
      "method": "GET",
      "path": "/{instance_id}/contacts/blocklist",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "blockContact": {
      "method": "POST",
      "path": "/{instance_id}/contacts/block-contact",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "query"
        }
      ],
      "unwrap": false
    },
    "unblockContact": {
      "method": "POST",
      "path": "/{instance_id}/contacts/unblock-contact",
      "body": false,
      "params": [
        {
          "name": "phone",
          "in": "query"
        }
      ],
      "unwrap": false
    },
    "contactVcard": {
      "method": "POST",
      "path": "/{instance_id}/contacts/vcard",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "getBatteryLevel": {
      "method": "GET",
      "path": "/{instance_id}/contacts/battery-level",
      "body": false,
      "params": [],
      "unwrap": false
    }
  },
  "groups": {
    "listGroups": {
      "method": "GET",
      "path": "/{instance_id}/groups",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "listGroupMembers": {
      "method": "GET",
      "path": "/{instance_id}/groups/{group_id}/members",
      "body": false,
      "params": [
        {
          "name": "group_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "commonGroups": {
      "method": "GET",
      "path": "/{instance_id}/groups/common/{wid}",
      "body": false,
      "params": [
        {
          "name": "wid",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "groupAdmins": {
      "method": "GET",
      "path": "/{instance_id}/groups/{group_id}/admins",
      "body": false,
      "params": [
        {
          "name": "group_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "groupInviteLink": {
      "method": "GET",
      "path": "/{instance_id}/groups/{group_id}/invite-link",
      "body": false,
      "params": [
        {
          "name": "group_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "groupRevokeLink": {
      "method": "POST",
      "path": "/{instance_id}/groups/{group_id}/revoke-link",
      "body": false,
      "params": [
        {
          "name": "group_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "groupMemberIds": {
      "method": "GET",
      "path": "/{instance_id}/groups/{group_id}/member-ids",
      "body": false,
      "params": [
        {
          "name": "group_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "createGroup": {
      "method": "POST",
      "path": "/{instance_id}/groups/create",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "leaveGroup": {
      "method": "POST",
      "path": "/{instance_id}/groups/leave",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "joinCode": {
      "method": "GET",
      "path": "/{instance_id}/groups/{group_id}/join-code",
      "body": false,
      "params": [
        {
          "name": "group_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "addParticipants": {
      "method": "POST",
      "path": "/{instance_id}/groups/add-participants",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "removeParticipants": {
      "method": "POST",
      "path": "/{instance_id}/groups/remove-participants",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "promoteParticipants": {
      "method": "POST",
      "path": "/{instance_id}/groups/promote-participants",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "demoteParticipants": {
      "method": "POST",
      "path": "/{instance_id}/groups/demote-participants",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "groupInfoFromInviteLink": {
      "method": "GET",
      "path": "/{instance_id}/groups/info-from-invite/{invite_code}",
      "body": false,
      "params": [
        {
          "name": "invite_code",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "groupDescription": {
      "method": "POST",
      "path": "/{instance_id}/groups/description",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "groupProperty": {
      "method": "POST",
      "path": "/{instance_id}/groups/property",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "groupSubject": {
      "method": "POST",
      "path": "/{instance_id}/groups/subject",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "messagesAdminsOnly": {
      "method": "POST",
      "path": "/{instance_id}/groups/messages-admins-only",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "groupPicture": {
      "method": "POST",
      "path": "/{instance_id}/groups/picture",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "changePrivacyGroup": {
      "method": "POST",
      "path": "/{instance_id}/groups/change-privacy",
      "body": true,
      "params": [],
      "unwrap": false
    }
  },
  "labels": {
    "getAllLabels": {
      "method": "GET",
      "path": "/{instance_id}/labels",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "addLabel": {
      "method": "POST",
      "path": "/{instance_id}/labels/add",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "addOrRemoveLabel": {
      "method": "POST",
      "path": "/{instance_id}/labels/add-or-remove",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "deleteAllLabels": {
      "method": "POST",
      "path": "/{instance_id}/labels/delete-all",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "deleteLabel": {
      "method": "POST",
      "path": "/{instance_id}/labels/delete/{label_id}",
      "body": false,
      "params": [
        {
          "name": "label_id",
          "in": "path"
        }
      ],
      "unwrap": false
    }
  },
  "media": {
    "platformFromMessage": {
      "method": "GET",
      "path": "/{instance_id}/media/platform-from-message/{message_id}",
      "body": false,
      "params": [
        {
          "name": "message_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "downloadMedia": {
      "method": "POST",
      "path": "/{instance_id}/media/download",
      "body": false,
      "params": [
        {
          "name": "messageId",
          "in": "query"
        }
      ],
      "unwrap": false
    }
  },
  "messages": {
    "sendTextMessage": {
      "method": "POST",
      "path": "/{instance_id}/messages/text",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendImageMessage": {
      "method": "POST",
      "path": "/{instance_id}/messages/image",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendLinkPreview": {
      "method": "POST",
      "path": "/{instance_id}/messages/link-preview",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendLocation": {
      "method": "POST",
      "path": "/{instance_id}/messages/location",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendFileBase64": {
      "method": "POST",
      "path": "/{instance_id}/messages/file-base64",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendVoiceBase64": {
      "method": "POST",
      "path": "/{instance_id}/messages/voice-base64",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "getMediaByMessage": {
      "method": "GET",
      "path": "/{instance_id}/messages/{message_id}/media",
      "body": false,
      "params": [
        {
          "name": "message_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "editMessage": {
      "method": "POST",
      "path": "/{instance_id}/messages/edit",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "forwardMessages": {
      "method": "POST",
      "path": "/{instance_id}/messages/forward",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "reactMessage": {
      "method": "POST",
      "path": "/{instance_id}/messages/react",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendReply": {
      "method": "POST",
      "path": "/{instance_id}/messages/reply",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendSticker": {
      "method": "POST",
      "path": "/{instance_id}/messages/sticker",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendMentioned": {
      "method": "POST",
      "path": "/{instance_id}/messages/mentioned",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendButtons": {
      "method": "POST",
      "path": "/{instance_id}/messages/buttons",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendListMessage": {
      "method": "POST",
      "path": "/{instance_id}/messages/list",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendOrderMessage": {
      "method": "POST",
      "path": "/{instance_id}/messages/order",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendPollMessage": {
      "method": "POST",
      "path": "/{instance_id}/messages/poll",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendStatusText": {
      "method": "POST",
      "path": "/{instance_id}/messages/status",
      "body": true,
      "params": [],
      "unwrap": false
    }
  },
  "misc": {
    "getPhoneNumber": {
      "method": "GET",
      "path": "/{instance_id}/misc/get-phone-number",
      "body": false,
      "params": [],
      "unwrap": false
    }
  },
  "presence": {
    "subscribePresence": {
      "method": "POST",
      "path": "/{instance_id}/presence/subscribe",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "setOnlinePresence": {
      "method": "POST",
      "path": "/{instance_id}/presence/set-online",
      "body": true,
      "params": [],
      "unwrap": false
    }
  },
  "products": {
    "getProducts": {
      "method": "GET",
      "path": "/{instance_id}/products",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "addProduct": {
      "method": "POST",
      "path": "/{instance_id}/products",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "getProductById": {
      "method": "GET",
      "path": "/{instance_id}/products/{product_id}",
      "body": false,
      "params": [
        {
          "name": "product_id",
          "in": "path"
        }
      ],
      "unwrap": false
    },
    "editProduct": {
      "method": "POST",
      "path": "/{instance_id}/products/edit",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "deleteProducts": {
      "method": "POST",
      "path": "/{instance_id}/products/delete",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "changeProductImage": {
      "method": "POST",
      "path": "/{instance_id}/products/image",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "addProductImage": {
      "method": "POST",
      "path": "/{instance_id}/products/image/add",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "removeProductImage": {
      "method": "POST",
      "path": "/{instance_id}/products/image/remove",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "setProductVisibility": {
      "method": "POST",
      "path": "/{instance_id}/products/visibility",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "setCartEnabled": {
      "method": "POST",
      "path": "/{instance_id}/products/cart-enabled",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "getCollections": {
      "method": "GET",
      "path": "/{instance_id}/products/collections",
      "body": false,
      "params": [],
      "unwrap": false
    },
    "createCollection": {
      "method": "POST",
      "path": "/{instance_id}/products/collections",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "editCollection": {
      "method": "POST",
      "path": "/{instance_id}/products/collections/edit",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "deleteCollection": {
      "method": "POST",
      "path": "/{instance_id}/products/collections/delete",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendLinkCatalog": {
      "method": "POST",
      "path": "/{instance_id}/products/send-link-catalog",
      "body": false,
      "params": [],
      "unwrap": false
    }
  },
  "sms": {
    "balance": {
      "method": "GET",
      "path": "/sms/balance",
      "body": false,
      "params": [],
      "unwrap": true
    },
    "senders": {
      "method": "GET",
      "path": "/sms/senders",
      "body": false,
      "params": [],
      "unwrap": true
    },
    "send": {
      "method": "POST",
      "path": "/sms/send",
      "body": true,
      "params": [],
      "unwrap": true
    },
    "sendBulk": {
      "method": "POST",
      "path": "/sms/send-bulk",
      "body": true,
      "params": [],
      "unwrap": true
    },
    "status": {
      "method": "GET",
      "path": "/sms/status/{message_x_id}",
      "body": false,
      "params": [
        {
          "name": "message_x_id",
          "in": "path"
        }
      ],
      "unwrap": true
    },
    "optOuts": {
      "method": "POST",
      "path": "/sms/opt-outs",
      "body": true,
      "params": [],
      "unwrap": true
    }
  },
  "stories": {
    "sendTextStorie": {
      "method": "POST",
      "path": "/{instance_id}/stories/text",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendImageStorie": {
      "method": "POST",
      "path": "/{instance_id}/stories/image",
      "body": true,
      "params": [],
      "unwrap": false
    },
    "sendVideoStorie": {
      "method": "POST",
      "path": "/{instance_id}/stories/video",
      "body": true,
      "params": [],
      "unwrap": false
    }
  }
} as const;
