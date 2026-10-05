# Public API methods

Generated from the backend routes. Base URL: `https://api.weezy.app/client/api/v1`.

## broadcasts

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).broadcasts.allBroadcasts` | `whatsapp(instance_id).broadcasts.all_broadcasts` | GET | `/{instance_id}/broadcasts` |

## chats

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).chats.allChats` | `whatsapp(instance_id).chats.all_chats` | GET | `/{instance_id}/chats` |
| `whatsapp(instanceId).chats.listChats` | `whatsapp(instance_id).chats.list_chats` | GET | `/{instance_id}/chats/list` |
| `whatsapp(instanceId).chats.unreadMessages` | `whatsapp(instance_id).chats.unread_messages` | GET | `/{instance_id}/chats/unread` |
| `whatsapp(instanceId).chats.typing` | `whatsapp(instance_id).chats.typing` | POST | `/{instance_id}/chats/typing` |
| `whatsapp(instanceId).chats.sendSeen` | `whatsapp(instance_id).chats.send_seen` | POST | `/{instance_id}/chats/send-seen` |
| `whatsapp(instanceId).chats.allChatsArchived` | `whatsapp(instance_id).chats.all_chats_archived` | GET | `/{instance_id}/chats/archived` |
| `whatsapp(instanceId).chats.allChatsWithMessages` | `whatsapp(instance_id).chats.all_chats_with_messages` | GET | `/{instance_id}/chats/with-messages` |
| `whatsapp(instanceId).chats.chatById` | `whatsapp(instance_id).chats.chat_by_id` | GET | `/{instance_id}/chats/by-id/{phone}` |
| `whatsapp(instanceId).chats.chatIsOnline` | `whatsapp(instance_id).chats.chat_is_online` | GET | `/{instance_id}/chats/is-online/{phone}` |
| `whatsapp(instanceId).chats.lastSeen` | `whatsapp(instance_id).chats.last_seen` | GET | `/{instance_id}/chats/last-seen/{phone}` |
| `whatsapp(instanceId).chats.listMutes` | `whatsapp(instance_id).chats.list_mutes` | GET | `/{instance_id}/chats/list-mutes/{mute_type}` |
| `whatsapp(instanceId).chats.loadMessagesInChat` | `whatsapp(instance_id).chats.load_messages_in_chat` | POST | `/{instance_id}/chats/load-messages` |
| `whatsapp(instanceId).chats.getMessages` | `whatsapp(instance_id).chats.get_messages` | GET | `/{instance_id}/chats/messages/{phone}` |
| `whatsapp(instanceId).chats.allNewMessages` | `whatsapp(instance_id).chats.all_new_messages` | GET | `/{instance_id}/chats/new` |
| `whatsapp(instanceId).chats.allUnreadMessages` | `whatsapp(instance_id).chats.all_unread_messages` | GET | `/{instance_id}/chats/all-unread` |
| `whatsapp(instanceId).chats.loadMessagesGet` | `whatsapp(instance_id).chats.load_messages_get` | GET | `/{instance_id}/chats/load-messages/{phone}` |
| `whatsapp(instanceId).chats.messageById` | `whatsapp(instance_id).chats.message_by_id` | GET | `/{instance_id}/chats/message-by-id/{message_id}` |
| `whatsapp(instanceId).chats.archiveChat` | `whatsapp(instance_id).chats.archive_chat` | POST | `/{instance_id}/chats/archive` |
| `whatsapp(instanceId).chats.archiveAllChats` | `whatsapp(instance_id).chats.archive_all_chats` | POST | `/{instance_id}/chats/archive-all` |
| `whatsapp(instanceId).chats.clearChat` | `whatsapp(instance_id).chats.clear_chat` | POST | `/{instance_id}/chats/clear` |
| `whatsapp(instanceId).chats.clearAllChats` | `whatsapp(instance_id).chats.clear_all_chats` | POST | `/{instance_id}/chats/clear-all` |
| `whatsapp(instanceId).chats.deleteChat` | `whatsapp(instance_id).chats.delete_chat` | POST | `/{instance_id}/chats/delete` |
| `whatsapp(instanceId).chats.deleteAllChats` | `whatsapp(instance_id).chats.delete_all_chats` | POST | `/{instance_id}/chats/delete-all` |
| `whatsapp(instanceId).chats.deleteMessage` | `whatsapp(instance_id).chats.delete_message` | POST | `/{instance_id}/chats/delete-message` |
| `whatsapp(instanceId).chats.markUnseen` | `whatsapp(instance_id).chats.mark_unseen` | POST | `/{instance_id}/chats/mark-unseen` |
| `whatsapp(instanceId).chats.pinChat` | `whatsapp(instance_id).chats.pin_chat` | POST | `/{instance_id}/chats/pin` |
| `whatsapp(instanceId).chats.chatState` | `whatsapp(instance_id).chats.chat_state` | POST | `/{instance_id}/chats/chat-state` |
| `whatsapp(instanceId).chats.chatRecording` | `whatsapp(instance_id).chats.chat_recording` | POST | `/{instance_id}/chats/recording` |
| `whatsapp(instanceId).chats.temporaryMessages` | `whatsapp(instance_id).chats.temporary_messages` | POST | `/{instance_id}/chats/temporary-messages` |
| `whatsapp(instanceId).chats.starMessage` | `whatsapp(instance_id).chats.star_message` | POST | `/{instance_id}/chats/star-message` |
| `whatsapp(instanceId).chats.reactions` | `whatsapp(instance_id).chats.reactions` | GET | `/{instance_id}/chats/reactions/{message_id}` |
| `whatsapp(instanceId).chats.votes` | `whatsapp(instance_id).chats.votes` | GET | `/{instance_id}/chats/votes/{message_id}` |
| `whatsapp(instanceId).chats.rejectCall` | `whatsapp(instance_id).chats.reject_call` | POST | `/{instance_id}/chats/reject-call` |
| `whatsapp(instanceId).chats.sendMute` | `whatsapp(instance_id).chats.send_mute` | POST | `/{instance_id}/chats/send-mute` |

## community

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).community.createCommunity` | `whatsapp(instance_id).community.create_community` | POST | `/{instance_id}/community/create` |
| `whatsapp(instanceId).community.deactivateCommunity` | `whatsapp(instance_id).community.deactivate_community` | POST | `/{instance_id}/community/deactivate` |
| `whatsapp(instanceId).community.addSubgroup` | `whatsapp(instance_id).community.add_subgroup` | POST | `/{instance_id}/community/add-subgroup` |
| `whatsapp(instanceId).community.removeSubgroup` | `whatsapp(instance_id).community.remove_subgroup` | POST | `/{instance_id}/community/remove-subgroup` |
| `whatsapp(instanceId).community.promoteParticipant` | `whatsapp(instance_id).community.promote_participant` | POST | `/{instance_id}/community/promote-participant` |
| `whatsapp(instanceId).community.demoteParticipant` | `whatsapp(instance_id).community.demote_participant` | POST | `/{instance_id}/community/demote-participant` |
| `whatsapp(instanceId).community.communityParticipants` | `whatsapp(instance_id).community.community_participants` | GET | `/{instance_id}/community/participants/{id}` |

## contacts

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).contacts.allContacts` | `whatsapp(instance_id).contacts.all_contacts` | GET | `/{instance_id}/contacts` |
| `whatsapp(instanceId).contacts.checkNumberStatus` | `whatsapp(instance_id).contacts.check_number_status` | GET | `/{instance_id}/contacts/check-number-status/{phone}` |
| `whatsapp(instanceId).contacts.getContact` | `whatsapp(instance_id).contacts.get_contact` | GET | `/{instance_id}/contacts/contact/{phone}` |
| `whatsapp(instanceId).contacts.profile` | `whatsapp(instance_id).contacts.profile` | GET | `/{instance_id}/contacts/profile/{phone}` |
| `whatsapp(instanceId).contacts.profilePic` | `whatsapp(instance_id).contacts.profile_pic` | GET | `/{instance_id}/contacts/profile-pic/{phone}` |
| `whatsapp(instanceId).contacts.profileStatus` | `whatsapp(instance_id).contacts.profile_status` | GET | `/{instance_id}/contacts/profile-status/{phone}` |
| `whatsapp(instanceId).contacts.blocklist` | `whatsapp(instance_id).contacts.blocklist` | GET | `/{instance_id}/contacts/blocklist` |
| `whatsapp(instanceId).contacts.blockContact` | `whatsapp(instance_id).contacts.block_contact` | POST | `/{instance_id}/contacts/block-contact` |
| `whatsapp(instanceId).contacts.unblockContact` | `whatsapp(instance_id).contacts.unblock_contact` | POST | `/{instance_id}/contacts/unblock-contact` |
| `whatsapp(instanceId).contacts.contactVcard` | `whatsapp(instance_id).contacts.contact_vcard` | POST | `/{instance_id}/contacts/vcard` |
| `whatsapp(instanceId).contacts.getBatteryLevel` | `whatsapp(instance_id).contacts.get_battery_level` | GET | `/{instance_id}/contacts/battery-level` |

## groups

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).groups.listGroups` | `whatsapp(instance_id).groups.list_groups` | GET | `/{instance_id}/groups` |
| `whatsapp(instanceId).groups.listGroupMembers` | `whatsapp(instance_id).groups.list_group_members` | GET | `/{instance_id}/groups/{group_id}/members` |
| `whatsapp(instanceId).groups.commonGroups` | `whatsapp(instance_id).groups.common_groups` | GET | `/{instance_id}/groups/common/{wid}` |
| `whatsapp(instanceId).groups.groupAdmins` | `whatsapp(instance_id).groups.group_admins` | GET | `/{instance_id}/groups/{group_id}/admins` |
| `whatsapp(instanceId).groups.groupInviteLink` | `whatsapp(instance_id).groups.group_invite_link` | GET | `/{instance_id}/groups/{group_id}/invite-link` |
| `whatsapp(instanceId).groups.groupRevokeLink` | `whatsapp(instance_id).groups.group_revoke_link` | POST | `/{instance_id}/groups/{group_id}/revoke-link` |
| `whatsapp(instanceId).groups.groupMemberIds` | `whatsapp(instance_id).groups.group_member_ids` | GET | `/{instance_id}/groups/{group_id}/member-ids` |
| `whatsapp(instanceId).groups.createGroup` | `whatsapp(instance_id).groups.create_group` | POST | `/{instance_id}/groups/create` |
| `whatsapp(instanceId).groups.leaveGroup` | `whatsapp(instance_id).groups.leave_group` | POST | `/{instance_id}/groups/leave` |
| `whatsapp(instanceId).groups.joinCode` | `whatsapp(instance_id).groups.join_code` | GET | `/{instance_id}/groups/{group_id}/join-code` |
| `whatsapp(instanceId).groups.addParticipants` | `whatsapp(instance_id).groups.add_participants` | POST | `/{instance_id}/groups/add-participants` |
| `whatsapp(instanceId).groups.removeParticipants` | `whatsapp(instance_id).groups.remove_participants` | POST | `/{instance_id}/groups/remove-participants` |
| `whatsapp(instanceId).groups.promoteParticipants` | `whatsapp(instance_id).groups.promote_participants` | POST | `/{instance_id}/groups/promote-participants` |
| `whatsapp(instanceId).groups.demoteParticipants` | `whatsapp(instance_id).groups.demote_participants` | POST | `/{instance_id}/groups/demote-participants` |
| `whatsapp(instanceId).groups.groupInfoFromInviteLink` | `whatsapp(instance_id).groups.group_info_from_invite_link` | GET | `/{instance_id}/groups/info-from-invite/{invite_code}` |
| `whatsapp(instanceId).groups.groupDescription` | `whatsapp(instance_id).groups.group_description` | POST | `/{instance_id}/groups/description` |
| `whatsapp(instanceId).groups.groupProperty` | `whatsapp(instance_id).groups.group_property` | POST | `/{instance_id}/groups/property` |
| `whatsapp(instanceId).groups.groupSubject` | `whatsapp(instance_id).groups.group_subject` | POST | `/{instance_id}/groups/subject` |
| `whatsapp(instanceId).groups.messagesAdminsOnly` | `whatsapp(instance_id).groups.messages_admins_only` | POST | `/{instance_id}/groups/messages-admins-only` |
| `whatsapp(instanceId).groups.groupPicture` | `whatsapp(instance_id).groups.group_picture` | POST | `/{instance_id}/groups/picture` |
| `whatsapp(instanceId).groups.changePrivacyGroup` | `whatsapp(instance_id).groups.change_privacy_group` | POST | `/{instance_id}/groups/change-privacy` |

## labels

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).labels.getAllLabels` | `whatsapp(instance_id).labels.get_all_labels` | GET | `/{instance_id}/labels` |
| `whatsapp(instanceId).labels.addLabel` | `whatsapp(instance_id).labels.add_label` | POST | `/{instance_id}/labels/add` |
| `whatsapp(instanceId).labels.addOrRemoveLabel` | `whatsapp(instance_id).labels.add_or_remove_label` | POST | `/{instance_id}/labels/add-or-remove` |
| `whatsapp(instanceId).labels.deleteAllLabels` | `whatsapp(instance_id).labels.delete_all_labels` | POST | `/{instance_id}/labels/delete-all` |
| `whatsapp(instanceId).labels.deleteLabel` | `whatsapp(instance_id).labels.delete_label` | POST | `/{instance_id}/labels/delete/{label_id}` |

## media

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).media.platformFromMessage` | `whatsapp(instance_id).media.platform_from_message` | GET | `/{instance_id}/media/platform-from-message/{message_id}` |
| `whatsapp(instanceId).media.downloadMedia` | `whatsapp(instance_id).media.download_media` | POST | `/{instance_id}/media/download` |

## messages

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).messages.sendTextMessage` | `whatsapp(instance_id).messages.send_text_message` | POST | `/{instance_id}/messages/text` |
| `whatsapp(instanceId).messages.sendImageMessage` | `whatsapp(instance_id).messages.send_image_message` | POST | `/{instance_id}/messages/image` |
| `whatsapp(instanceId).messages.sendLinkPreview` | `whatsapp(instance_id).messages.send_link_preview` | POST | `/{instance_id}/messages/link-preview` |
| `whatsapp(instanceId).messages.sendLocation` | `whatsapp(instance_id).messages.send_location` | POST | `/{instance_id}/messages/location` |
| `whatsapp(instanceId).messages.sendFileBase64` | `whatsapp(instance_id).messages.send_file_base64` | POST | `/{instance_id}/messages/file-base64` |
| `whatsapp(instanceId).messages.sendVoiceBase64` | `whatsapp(instance_id).messages.send_voice_base64` | POST | `/{instance_id}/messages/voice-base64` |
| `whatsapp(instanceId).messages.getMediaByMessage` | `whatsapp(instance_id).messages.get_media_by_message` | GET | `/{instance_id}/messages/{message_id}/media` |
| `whatsapp(instanceId).messages.editMessage` | `whatsapp(instance_id).messages.edit_message` | POST | `/{instance_id}/messages/edit` |
| `whatsapp(instanceId).messages.forwardMessages` | `whatsapp(instance_id).messages.forward_messages` | POST | `/{instance_id}/messages/forward` |
| `whatsapp(instanceId).messages.reactMessage` | `whatsapp(instance_id).messages.react_message` | POST | `/{instance_id}/messages/react` |
| `whatsapp(instanceId).messages.sendReply` | `whatsapp(instance_id).messages.send_reply` | POST | `/{instance_id}/messages/reply` |
| `whatsapp(instanceId).messages.sendSticker` | `whatsapp(instance_id).messages.send_sticker` | POST | `/{instance_id}/messages/sticker` |
| `whatsapp(instanceId).messages.sendMentioned` | `whatsapp(instance_id).messages.send_mentioned` | POST | `/{instance_id}/messages/mentioned` |
| `whatsapp(instanceId).messages.sendButtons` | `whatsapp(instance_id).messages.send_buttons` | POST | `/{instance_id}/messages/buttons` |
| `whatsapp(instanceId).messages.sendListMessage` | `whatsapp(instance_id).messages.send_list_message` | POST | `/{instance_id}/messages/list` |
| `whatsapp(instanceId).messages.sendOrderMessage` | `whatsapp(instance_id).messages.send_order_message` | POST | `/{instance_id}/messages/order` |
| `whatsapp(instanceId).messages.sendPollMessage` | `whatsapp(instance_id).messages.send_poll_message` | POST | `/{instance_id}/messages/poll` |
| `whatsapp(instanceId).messages.sendStatusText` | `whatsapp(instance_id).messages.send_status_text` | POST | `/{instance_id}/messages/status` |

## misc

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).misc.getPhoneNumber` | `whatsapp(instance_id).misc.get_phone_number` | GET | `/{instance_id}/misc/get-phone-number` |

## presence

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).presence.subscribePresence` | `whatsapp(instance_id).presence.subscribe_presence` | POST | `/{instance_id}/presence/subscribe` |
| `whatsapp(instanceId).presence.setOnlinePresence` | `whatsapp(instance_id).presence.set_online_presence` | POST | `/{instance_id}/presence/set-online` |

## products

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).products.getProducts` | `whatsapp(instance_id).products.get_products` | GET | `/{instance_id}/products` |
| `whatsapp(instanceId).products.addProduct` | `whatsapp(instance_id).products.add_product` | POST | `/{instance_id}/products` |
| `whatsapp(instanceId).products.getProductById` | `whatsapp(instance_id).products.get_product_by_id` | GET | `/{instance_id}/products/{product_id}` |
| `whatsapp(instanceId).products.editProduct` | `whatsapp(instance_id).products.edit_product` | POST | `/{instance_id}/products/edit` |
| `whatsapp(instanceId).products.deleteProducts` | `whatsapp(instance_id).products.delete_products` | POST | `/{instance_id}/products/delete` |
| `whatsapp(instanceId).products.changeProductImage` | `whatsapp(instance_id).products.change_product_image` | POST | `/{instance_id}/products/image` |
| `whatsapp(instanceId).products.addProductImage` | `whatsapp(instance_id).products.add_product_image` | POST | `/{instance_id}/products/image/add` |
| `whatsapp(instanceId).products.removeProductImage` | `whatsapp(instance_id).products.remove_product_image` | POST | `/{instance_id}/products/image/remove` |
| `whatsapp(instanceId).products.setProductVisibility` | `whatsapp(instance_id).products.set_product_visibility` | POST | `/{instance_id}/products/visibility` |
| `whatsapp(instanceId).products.setCartEnabled` | `whatsapp(instance_id).products.set_cart_enabled` | POST | `/{instance_id}/products/cart-enabled` |
| `whatsapp(instanceId).products.getCollections` | `whatsapp(instance_id).products.get_collections` | GET | `/{instance_id}/products/collections` |
| `whatsapp(instanceId).products.createCollection` | `whatsapp(instance_id).products.create_collection` | POST | `/{instance_id}/products/collections` |
| `whatsapp(instanceId).products.editCollection` | `whatsapp(instance_id).products.edit_collection` | POST | `/{instance_id}/products/collections/edit` |
| `whatsapp(instanceId).products.deleteCollection` | `whatsapp(instance_id).products.delete_collection` | POST | `/{instance_id}/products/collections/delete` |
| `whatsapp(instanceId).products.sendLinkCatalog` | `whatsapp(instance_id).products.send_link_catalog` | POST | `/{instance_id}/products/send-link-catalog` |

## sms

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `sms.balance` | `sms.balance` | GET | `/sms/balance` |
| `sms.senders` | `sms.senders` | GET | `/sms/senders` |
| `sms.send` | `sms.send` | POST | `/sms/send` |
| `sms.sendBulk` | `sms.send_bulk` | POST | `/sms/send-bulk` |
| `sms.status` | `sms.status` | GET | `/sms/status/{message_x_id}` |
| `sms.optOuts` | `sms.opt_outs` | POST | `/sms/opt-outs` |

## stories

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `whatsapp(instanceId).stories.sendTextStorie` | `whatsapp(instance_id).stories.send_text_storie` | POST | `/{instance_id}/stories/text` |
| `whatsapp(instanceId).stories.sendImageStorie` | `whatsapp(instance_id).stories.send_image_storie` | POST | `/{instance_id}/stories/image` |
| `whatsapp(instanceId).stories.sendVideoStorie` | `whatsapp(instance_id).stories.send_video_storie` | POST | `/{instance_id}/stories/video` |

