"""Generated resource methods."""
from __future__ import annotations
from typing import Any, Dict, List, Literal, Union
from ._transport import segment
from .types import *

class BroadcastsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def all_broadcasts(self) -> List['SimpleOut']:
        """All broadcast lists."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/broadcasts', body=None, query={}, unwrap=False)

class ChatsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def all_chats(self) -> List['SimpleOut']:
        """All chats."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats', body=None, query={}, unwrap=False)

    def list_chats(self) -> List['SimpleOut']:
        """List chats."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/list', body=None, query={}, unwrap=False)

    def unread_messages(self) -> List['SimpleOut']:
        """Unread messages."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/unread', body=None, query={}, unwrap=False)

    def typing(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Typing state."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/typing', body=body, query={}, unwrap=False)

    def send_seen(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Send seen."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/send-seen', body=body, query={}, unwrap=False)

    def all_chats_archived(self) -> List['SimpleOut']:
        """All archived chats."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/archived', body=None, query={}, unwrap=False)

    def all_chats_with_messages(self) -> List['SimpleOut']:
        """All chats with messages."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/with-messages', body=None, query={}, unwrap=False)

    def chat_by_id(self, *, phone: str) -> 'SimpleOut':
        """Chat by id."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/by-id/{segment(phone)}', body=None, query={}, unwrap=False)

    def chat_is_online(self, *, phone: str) -> 'SimpleOut':
        """Chat is online."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/is-online/{segment(phone)}', body=None, query={}, unwrap=False)

    def last_seen(self, *, phone: str) -> 'SimpleOut':
        """Last seen."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/last-seen/{segment(phone)}', body=None, query={}, unwrap=False)

    def list_mutes(self, *, mute_type: str) -> List['SimpleOut']:
        """List mutes."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/list-mutes/{segment(mute_type)}', body=None, query={}, unwrap=False)

    def load_messages_in_chat(self, *, body: 'LoadMessagesInChatIn') -> List['SimpleOut']:
        """Load messages in chat."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/load-messages', body=body, query={}, unwrap=False)

    def get_messages(self, *, phone: str) -> List['SimpleOut']:
        """Get messages."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/messages/{segment(phone)}', body=None, query={}, unwrap=False)

    def all_new_messages(self) -> List['SimpleOut']:
        """All new messages."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/new', body=None, query={}, unwrap=False)

    def all_unread_messages(self) -> List['SimpleOut']:
        """All unread messages."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/all-unread', body=None, query={}, unwrap=False)

    def load_messages_get(self, *, phone: str, count: int = None) -> List['SimpleOut']:
        """Load messages in chat (GET)."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/load-messages/{segment(phone)}', body=None, query={'count': count}, unwrap=False)

    def message_by_id(self, *, message_id: str) -> 'SimpleOut':
        """Get message by id."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/message-by-id/{segment(message_id)}', body=None, query={}, unwrap=False)

    def archive_chat(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Archive chat."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/archive', body=body, query={}, unwrap=False)

    def archive_all_chats(self) -> 'ActionResultOut':
        """Archive all chats."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/archive-all', body=None, query={}, unwrap=False)

    def clear_chat(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Clear chat."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/clear', body=body, query={}, unwrap=False)

    def clear_all_chats(self) -> 'ActionResultOut':
        """Clear all chats."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/clear-all', body=None, query={}, unwrap=False)

    def delete_chat(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Delete chat."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/delete', body=body, query={}, unwrap=False)

    def delete_all_chats(self) -> 'ActionResultOut':
        """Delete all chats."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/delete-all', body=None, query={}, unwrap=False)

    def delete_message(self, *, body: 'MessageIdIn') -> 'ActionResultOut':
        """Delete message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/delete-message', body=body, query={}, unwrap=False)

    def mark_unseen(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Mark unseen."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/mark-unseen', body=body, query={}, unwrap=False)

    def pin_chat(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Pin chat."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/pin', body=body, query={}, unwrap=False)

    def chat_state(self, *, body: 'ChatStateIn') -> 'ActionResultOut':
        """Set chat state."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/chat-state', body=body, query={}, unwrap=False)

    def chat_recording(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Recording state."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/recording', body=body, query={}, unwrap=False)

    def temporary_messages(self, *, body: 'TemporaryMessagesIn') -> 'ActionResultOut':
        """Set temporary messages."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/temporary-messages', body=body, query={}, unwrap=False)

    def star_message(self, *, body: 'StarMessageIn') -> 'ActionResultOut':
        """Star a message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/star-message', body=body, query={}, unwrap=False)

    def reactions(self, *, message_id: str) -> List['SimpleOut']:
        """Get reactions for message."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/reactions/{segment(message_id)}', body=None, query={}, unwrap=False)

    def votes(self, *, message_id: str) -> List['SimpleOut']:
        """Get votes for message."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/chats/votes/{segment(message_id)}', body=None, query={}, unwrap=False)

    def reject_call(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Reject call."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/reject-call', body=body, query={}, unwrap=False)

    def send_mute(self, *, body: 'SendMuteIn') -> 'ActionResultOut':
        """Send mute."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/chats/send-mute', body=body, query={}, unwrap=False)

class CommunityAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def create_community(self, *, body: 'CreateCommunityIn') -> 'ActionResultOut':
        """Create community."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/community/create', body=body, query={}, unwrap=False)

    def deactivate_community(self, *, body: 'CommunityIdIn') -> 'ActionResultOut':
        """Deactivate community."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/community/deactivate', body=body, query={}, unwrap=False)

    def add_subgroup(self, *, body: 'CommunitySubgroupsIn') -> 'ActionResultOut':
        """Add subgroups to community."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/community/add-subgroup', body=body, query={}, unwrap=False)

    def remove_subgroup(self, *, body: 'CommunitySubgroupsIn') -> 'ActionResultOut':
        """Remove subgroups from community."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/community/remove-subgroup', body=body, query={}, unwrap=False)

    def promote_participant(self, *, body: 'CommunityParticipantsIn') -> 'ActionResultOut':
        """Promote community participants."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/community/promote-participant', body=body, query={}, unwrap=False)

    def demote_participant(self, *, body: 'CommunityParticipantsIn') -> 'ActionResultOut':
        """Demote community participants."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/community/demote-participant', body=body, query={}, unwrap=False)

    def community_participants(self, *, id: str) -> List['SimpleOut']:
        """List community participants."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/community/participants/{segment(id)}', body=None, query={}, unwrap=False)

class ContactsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def all_contacts(self) -> List['ContactOut']:
        """All contacts."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/contacts', body=None, query={}, unwrap=False)

    def check_number_status(self, *, phone: str) -> 'CheckNumberStatusOut':
        """Check number status."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/contacts/check-number-status/{segment(phone)}', body=None, query={}, unwrap=False)

    def get_contact(self, *, phone: str) -> 'ContactOut':
        """Get contact by phone."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/contacts/contact/{segment(phone)}', body=None, query={}, unwrap=False)

    def profile(self, *, phone: str) -> 'ProfileOut':
        """Get profile."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/contacts/profile/{segment(phone)}', body=None, query={}, unwrap=False)

    def profile_pic(self, *, phone: str) -> 'ProfilePicOut':
        """Get profile picture."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/contacts/profile-pic/{segment(phone)}', body=None, query={}, unwrap=False)

    def profile_status(self, *, phone: str) -> 'ProfileOut':
        """Get profile status."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/contacts/profile-status/{segment(phone)}', body=None, query={}, unwrap=False)

    def blocklist(self) -> List[str]:
        """Get block list."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/contacts/blocklist', body=None, query={}, unwrap=False)

    def block_contact(self, *, phone: str) -> 'ActionResultOut':
        """Block contact."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/contacts/block-contact', body=None, query={'phone': phone}, unwrap=False)

    def unblock_contact(self, *, phone: str) -> 'ActionResultOut':
        """Unblock contact."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/contacts/unblock-contact', body=None, query={'phone': phone}, unwrap=False)

    def contact_vcard(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Send contact vCard."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/contacts/vcard', body=body, query={}, unwrap=False)

    def get_battery_level(self) -> Dict[str, Any]:
        """Get battery level."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/contacts/battery-level', body=None, query={}, unwrap=False)

class GroupsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def list_groups(self) -> List['SimpleOut']:
        """List groups."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/groups', body=None, query={}, unwrap=False)

    def list_group_members(self, *, group_id: str) -> List['SimpleOut']:
        """List group members."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/members', body=None, query={}, unwrap=False)

    def common_groups(self, *, wid: str) -> List['SimpleOut']:
        """Common groups with wid."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/groups/common/{segment(wid)}', body=None, query={}, unwrap=False)

    def group_admins(self, *, group_id: str) -> List['SimpleOut']:
        """Group admins."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/admins', body=None, query={}, unwrap=False)

    def group_invite_link(self, *, group_id: str) -> 'SimpleOut':
        """Invite link."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/invite-link', body=None, query={}, unwrap=False)

    def group_revoke_link(self, *, group_id: str) -> 'ActionResultOut':
        """Revoke invite link."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/revoke-link', body=None, query={}, unwrap=False)

    def group_member_ids(self, *, group_id: str) -> List[str]:
        """Group member IDs."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/member-ids', body=None, query={}, unwrap=False)

    def create_group(self, *, body: 'CreateGroupIn') -> 'ActionResultOut':
        """Create group."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/create', body=body, query={}, unwrap=False)

    def leave_group(self, *, body: 'LeaveGroupIn') -> 'ActionResultOut':
        """Leave group."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/leave', body=body, query={}, unwrap=False)

    def join_code(self, *, group_id: str) -> 'SimpleOut':
        """Get join code."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/join-code', body=None, query={}, unwrap=False)

    def add_participants(self, *, body: 'ParticipantsIn') -> 'ActionResultOut':
        """Add participants."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/add-participants', body=body, query={}, unwrap=False)

    def remove_participants(self, *, body: 'ParticipantsIn') -> 'ActionResultOut':
        """Remove participants."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/remove-participants', body=body, query={}, unwrap=False)

    def promote_participants(self, *, body: 'ParticipantsIn') -> 'ActionResultOut':
        """Promote participants."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/promote-participants', body=body, query={}, unwrap=False)

    def demote_participants(self, *, body: 'ParticipantsIn') -> 'ActionResultOut':
        """Demote participants."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/demote-participants', body=body, query={}, unwrap=False)

    def group_info_from_invite_link(self, *, invite_code: str) -> 'SimpleOut':
        """Group info from invite link."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/groups/info-from-invite/{segment(invite_code)}', body=None, query={}, unwrap=False)

    def group_description(self, *, body: 'GroupDescriptionIn') -> 'ActionResultOut':
        """Set group description."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/description', body=body, query={}, unwrap=False)

    def group_property(self, *, body: 'GroupPropertyIn') -> 'ActionResultOut':
        """Set group property."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/property', body=body, query={}, unwrap=False)

    def group_subject(self, *, body: 'GroupSubjectIn') -> 'ActionResultOut':
        """Set group subject."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/subject', body=body, query={}, unwrap=False)

    def messages_admins_only(self, *, body: 'MessagesAdminsOnlyIn') -> 'ActionResultOut':
        """Toggle messages only for admins."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/messages-admins-only', body=body, query={}, unwrap=False)

    def group_picture(self, *, body: 'GroupPicIn') -> 'ActionResultOut':
        """Set group picture."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/picture', body=body, query={}, unwrap=False)

    def change_privacy_group(self, *, body: 'ChangePrivacyGroupIn') -> 'ActionResultOut':
        """Change privacy of group."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/groups/change-privacy', body=body, query={}, unwrap=False)

class LabelsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def get_all_labels(self) -> List['SimpleOut']:
        """Get all labels."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/labels', body=None, query={}, unwrap=False)

    def add_label(self, *, body: 'AddLabelIn') -> 'ActionResultOut':
        """Add new label."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/labels/add', body=body, query={}, unwrap=False)

    def add_or_remove_label(self, *, body: 'AddOrRemoveLabelIn') -> 'ActionResultOut':
        """Add or remove label on chats."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/labels/add-or-remove', body=body, query={}, unwrap=False)

    def delete_all_labels(self) -> 'ActionResultOut':
        """Delete all labels."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/labels/delete-all', body=None, query={}, unwrap=False)

    def delete_label(self, *, label_id: str) -> 'ActionResultOut':
        """Delete label by id."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/labels/delete/{segment(label_id)}', body=None, query={}, unwrap=False)

class MediaAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def platform_from_message(self, *, message_id: str) -> 'SimpleOut':
        """Get platform from message."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/media/platform-from-message/{segment(message_id)}', body=None, query={}, unwrap=False)

    def download_media(self, *, messageId: str) -> 'SimpleOut':
        """Download media by message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/media/download', body=None, query={'messageId': messageId}, unwrap=False)

class MessagesAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def send_text_message(self, *, body: 'MessageTextIn') -> 'ActionResultOut':
        """Send text message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/text', body=body, query={}, unwrap=False)

    def send_image_message(self, *, body: 'MessageImageIn') -> 'ActionResultOut':
        """Send image (base64)."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/image', body=body, query={}, unwrap=False)

    def send_link_preview(self, *, body: 'LinkPreviewIn') -> 'ActionResultOut':
        """Send link preview."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/link-preview', body=body, query={}, unwrap=False)

    def send_location(self, *, body: 'LocationIn') -> 'ActionResultOut':
        """Send location."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/location', body=body, query={}, unwrap=False)

    def send_file_base64(self, *, body: 'FileBase64In') -> 'ActionResultOut':
        """Send file base64."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/file-base64', body=body, query={}, unwrap=False)

    def send_voice_base64(self, *, body: 'VoiceBase64In') -> 'ActionResultOut':
        """Send voice base64."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/voice-base64', body=body, query={}, unwrap=False)

    def get_media_by_message(self, *, message_id: str) -> 'SimpleOut':
        """Get media by message id."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/messages/{segment(message_id)}/media', body=None, query={}, unwrap=False)

    def edit_message(self, *, body: 'EditMessageIn') -> 'ActionResultOut':
        """Edit a message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/edit', body=body, query={}, unwrap=False)

    def forward_messages(self, *, body: 'ForwardMessagesIn') -> 'ActionResultOut':
        """Forward messages."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/forward', body=body, query={}, unwrap=False)

    def react_message(self, *, body: 'ReactMessageIn') -> 'ActionResultOut':
        """React to a message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/react', body=body, query={}, unwrap=False)

    def send_reply(self, *, body: 'ReplyMessageIn') -> 'ActionResultOut':
        """Send reply message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/reply', body=body, query={}, unwrap=False)

    def send_sticker(self, *, body: 'StickerIn') -> 'ActionResultOut':
        """Send sticker (base64)."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/sticker', body=body, query={}, unwrap=False)

    def send_mentioned(self, *, body: 'MentionedIn') -> 'ActionResultOut':
        """Send mentioned message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/mentioned', body=body, query={}, unwrap=False)

    def send_buttons(self, *, body: 'ButtonsIn') -> 'ActionResultOut':
        """Send buttons message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/buttons', body=body, query={}, unwrap=False)

    def send_list_message(self, *, body: 'ListMessageIn') -> 'ActionResultOut':
        """Send list message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/list', body=body, query={}, unwrap=False)

    def send_order_message(self, *, body: 'OrderMessageIn') -> 'ActionResultOut':
        """Send order message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/order', body=body, query={}, unwrap=False)

    def send_poll_message(self, *, body: 'PollMessageIn') -> 'ActionResultOut':
        """Send poll message."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/poll', body=body, query={}, unwrap=False)

    def send_status_text(self, *, body: 'SendStatusIn') -> 'ActionResultOut':
        """Send profile status text."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/messages/status', body=body, query={}, unwrap=False)

class MiscAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def get_phone_number(self) -> 'SimpleOut':
        """Get current account phone number."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/misc/get-phone-number', body=None, query={}, unwrap=False)

class PresenceAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def subscribe_presence(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Subscribe presence."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/presence/subscribe', body=body, query={}, unwrap=False)

    def set_online_presence(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Set online presence."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/presence/set-online', body=body, query={}, unwrap=False)

class ProductsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def get_products(self) -> List['SimpleOut']:
        """Get products."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/products', body=None, query={}, unwrap=False)

    def add_product(self, *, body: 'AddProductIn') -> 'ActionResultOut':
        """Add product."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products', body=body, query={}, unwrap=False)

    def get_product_by_id(self, *, product_id: str) -> 'SimpleOut':
        """Get product by id."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/products/{segment(product_id)}', body=None, query={}, unwrap=False)

    def edit_product(self, *, body: 'EditProductIn') -> 'ActionResultOut':
        """Edit product."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/edit', body=body, query={}, unwrap=False)

    def delete_products(self, *, body: 'DeleteProductsIn') -> 'ActionResultOut':
        """Delete products."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/delete', body=body, query={}, unwrap=False)

    def change_product_image(self, *, body: 'ProductImageIn') -> 'ActionResultOut':
        """Change product image."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/image', body=body, query={}, unwrap=False)

    def add_product_image(self, *, body: 'ProductImageIn') -> 'ActionResultOut':
        """Add product image."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/image/add', body=body, query={}, unwrap=False)

    def remove_product_image(self, *, body: 'ProductImageIn') -> 'ActionResultOut':
        """Remove product image."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/image/remove', body=body, query={}, unwrap=False)

    def set_product_visibility(self, *, body: 'ProductVisibilityIn') -> 'ActionResultOut':
        """Set product visibility."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/visibility', body=body, query={}, unwrap=False)

    def set_cart_enabled(self, *, body: 'SetCartEnabledIn') -> 'ActionResultOut':
        """Enable/disable cart."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/cart-enabled', body=body, query={}, unwrap=False)

    def get_collections(self) -> List['SimpleOut']:
        """Get collections."""
        return self._client.request('GET', f'/{segment(self._instance_id)}/products/collections', body=None, query={}, unwrap=False)

    def create_collection(self, *, body: 'CreateCollectionIn') -> 'ActionResultOut':
        """Create collection."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/collections', body=body, query={}, unwrap=False)

    def edit_collection(self, *, body: 'EditCollectionIn') -> 'ActionResultOut':
        """Edit collection."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/collections/edit', body=body, query={}, unwrap=False)

    def delete_collection(self, *, body: 'DeleteCollectionIn') -> 'ActionResultOut':
        """Delete collection."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/collections/delete', body=body, query={}, unwrap=False)

    def send_link_catalog(self) -> 'ActionResultOut':
        """Send link catalog."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/products/send-link-catalog', body=None, query={}, unwrap=False)

class SmsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def balance(self) -> 'WalletOut':
        """Remaining wallet balance."""
        return self._client.request('GET', f'/sms/balance', body=None, query={}, unwrap=True)

    def senders(self) -> Dict[str, Any]:
        """Sender IDs available for sending."""
        return self._client.request('GET', f'/sms/senders', body=None, query={}, unwrap=True)

    def send(self, *, body: 'SmsSendIn') -> 'SmsMessageOut':
        """Send one SMS."""
        return self._client.request('POST', f'/sms/send', body=body, query={}, unwrap=True)

    def send_bulk(self, *, body: 'SmsBulkSendIn') -> 'SmsBulkSendOut':
        """Send the same SMS to many recipients."""
        return self._client.request('POST', f'/sms/send-bulk', body=body, query={}, unwrap=True)

    def status(self, *, message_x_id: str) -> 'SmsMessageOut':
        """Get the delivery status of one SMS."""
        return self._client.request('GET', f'/sms/status/{segment(message_x_id)}', body=None, query={}, unwrap=True)

    def opt_outs(self, *, body: 'SmsOptOutIn') -> Dict[str, Any]:
        """Unsubscribe numbers (excluded from all future sends)."""
        return self._client.request('POST', f'/sms/opt-outs', body=body, query={}, unwrap=True)

class StoriesAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    def send_text_storie(self, *, body: 'MessageTextIn') -> 'ActionResultOut':
        """Send text storie."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/stories/text', body=body, query={}, unwrap=False)

    def send_image_storie(self, *, body: 'MessageImageIn') -> 'ActionResultOut':
        """Send image storie (base64)."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/stories/image', body=body, query={}, unwrap=False)

    def send_video_storie(self, *, body: 'MessageImageIn') -> 'ActionResultOut':
        """Send video storie (base64)."""
        return self._client.request('POST', f'/{segment(self._instance_id)}/stories/video', body=body, query={}, unwrap=False)

class WhatsAppAPI:
    def __init__(self, client, instance_id):
        self.broadcasts = BroadcastsAPI(client, instance_id)
        self.chats = ChatsAPI(client, instance_id)
        self.community = CommunityAPI(client, instance_id)
        self.contacts = ContactsAPI(client, instance_id)
        self.groups = GroupsAPI(client, instance_id)
        self.labels = LabelsAPI(client, instance_id)
        self.media = MediaAPI(client, instance_id)
        self.messages = MessagesAPI(client, instance_id)
        self.misc = MiscAPI(client, instance_id)
        self.presence = PresenceAPI(client, instance_id)
        self.products = ProductsAPI(client, instance_id)
        self.stories = StoriesAPI(client, instance_id)

class AsyncBroadcastsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def all_broadcasts(self) -> List['SimpleOut']:
        """All broadcast lists."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/broadcasts', body=None, query={}, unwrap=False)

class AsyncChatsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def all_chats(self) -> List['SimpleOut']:
        """All chats."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats', body=None, query={}, unwrap=False)

    async def list_chats(self) -> List['SimpleOut']:
        """List chats."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/list', body=None, query={}, unwrap=False)

    async def unread_messages(self) -> List['SimpleOut']:
        """Unread messages."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/unread', body=None, query={}, unwrap=False)

    async def typing(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Typing state."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/typing', body=body, query={}, unwrap=False)

    async def send_seen(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Send seen."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/send-seen', body=body, query={}, unwrap=False)

    async def all_chats_archived(self) -> List['SimpleOut']:
        """All archived chats."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/archived', body=None, query={}, unwrap=False)

    async def all_chats_with_messages(self) -> List['SimpleOut']:
        """All chats with messages."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/with-messages', body=None, query={}, unwrap=False)

    async def chat_by_id(self, *, phone: str) -> 'SimpleOut':
        """Chat by id."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/by-id/{segment(phone)}', body=None, query={}, unwrap=False)

    async def chat_is_online(self, *, phone: str) -> 'SimpleOut':
        """Chat is online."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/is-online/{segment(phone)}', body=None, query={}, unwrap=False)

    async def last_seen(self, *, phone: str) -> 'SimpleOut':
        """Last seen."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/last-seen/{segment(phone)}', body=None, query={}, unwrap=False)

    async def list_mutes(self, *, mute_type: str) -> List['SimpleOut']:
        """List mutes."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/list-mutes/{segment(mute_type)}', body=None, query={}, unwrap=False)

    async def load_messages_in_chat(self, *, body: 'LoadMessagesInChatIn') -> List['SimpleOut']:
        """Load messages in chat."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/load-messages', body=body, query={}, unwrap=False)

    async def get_messages(self, *, phone: str) -> List['SimpleOut']:
        """Get messages."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/messages/{segment(phone)}', body=None, query={}, unwrap=False)

    async def all_new_messages(self) -> List['SimpleOut']:
        """All new messages."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/new', body=None, query={}, unwrap=False)

    async def all_unread_messages(self) -> List['SimpleOut']:
        """All unread messages."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/all-unread', body=None, query={}, unwrap=False)

    async def load_messages_get(self, *, phone: str, count: int = None) -> List['SimpleOut']:
        """Load messages in chat (GET)."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/load-messages/{segment(phone)}', body=None, query={'count': count}, unwrap=False)

    async def message_by_id(self, *, message_id: str) -> 'SimpleOut':
        """Get message by id."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/message-by-id/{segment(message_id)}', body=None, query={}, unwrap=False)

    async def archive_chat(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Archive chat."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/archive', body=body, query={}, unwrap=False)

    async def archive_all_chats(self) -> 'ActionResultOut':
        """Archive all chats."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/archive-all', body=None, query={}, unwrap=False)

    async def clear_chat(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Clear chat."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/clear', body=body, query={}, unwrap=False)

    async def clear_all_chats(self) -> 'ActionResultOut':
        """Clear all chats."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/clear-all', body=None, query={}, unwrap=False)

    async def delete_chat(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Delete chat."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/delete', body=body, query={}, unwrap=False)

    async def delete_all_chats(self) -> 'ActionResultOut':
        """Delete all chats."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/delete-all', body=None, query={}, unwrap=False)

    async def delete_message(self, *, body: 'MessageIdIn') -> 'ActionResultOut':
        """Delete message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/delete-message', body=body, query={}, unwrap=False)

    async def mark_unseen(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Mark unseen."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/mark-unseen', body=body, query={}, unwrap=False)

    async def pin_chat(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Pin chat."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/pin', body=body, query={}, unwrap=False)

    async def chat_state(self, *, body: 'ChatStateIn') -> 'ActionResultOut':
        """Set chat state."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/chat-state', body=body, query={}, unwrap=False)

    async def chat_recording(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Recording state."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/recording', body=body, query={}, unwrap=False)

    async def temporary_messages(self, *, body: 'TemporaryMessagesIn') -> 'ActionResultOut':
        """Set temporary messages."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/temporary-messages', body=body, query={}, unwrap=False)

    async def star_message(self, *, body: 'StarMessageIn') -> 'ActionResultOut':
        """Star a message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/star-message', body=body, query={}, unwrap=False)

    async def reactions(self, *, message_id: str) -> List['SimpleOut']:
        """Get reactions for message."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/reactions/{segment(message_id)}', body=None, query={}, unwrap=False)

    async def votes(self, *, message_id: str) -> List['SimpleOut']:
        """Get votes for message."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/chats/votes/{segment(message_id)}', body=None, query={}, unwrap=False)

    async def reject_call(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Reject call."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/reject-call', body=body, query={}, unwrap=False)

    async def send_mute(self, *, body: 'SendMuteIn') -> 'ActionResultOut':
        """Send mute."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/chats/send-mute', body=body, query={}, unwrap=False)

class AsyncCommunityAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def create_community(self, *, body: 'CreateCommunityIn') -> 'ActionResultOut':
        """Create community."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/community/create', body=body, query={}, unwrap=False)

    async def deactivate_community(self, *, body: 'CommunityIdIn') -> 'ActionResultOut':
        """Deactivate community."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/community/deactivate', body=body, query={}, unwrap=False)

    async def add_subgroup(self, *, body: 'CommunitySubgroupsIn') -> 'ActionResultOut':
        """Add subgroups to community."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/community/add-subgroup', body=body, query={}, unwrap=False)

    async def remove_subgroup(self, *, body: 'CommunitySubgroupsIn') -> 'ActionResultOut':
        """Remove subgroups from community."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/community/remove-subgroup', body=body, query={}, unwrap=False)

    async def promote_participant(self, *, body: 'CommunityParticipantsIn') -> 'ActionResultOut':
        """Promote community participants."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/community/promote-participant', body=body, query={}, unwrap=False)

    async def demote_participant(self, *, body: 'CommunityParticipantsIn') -> 'ActionResultOut':
        """Demote community participants."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/community/demote-participant', body=body, query={}, unwrap=False)

    async def community_participants(self, *, id: str) -> List['SimpleOut']:
        """List community participants."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/community/participants/{segment(id)}', body=None, query={}, unwrap=False)

class AsyncContactsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def all_contacts(self) -> List['ContactOut']:
        """All contacts."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/contacts', body=None, query={}, unwrap=False)

    async def check_number_status(self, *, phone: str) -> 'CheckNumberStatusOut':
        """Check number status."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/contacts/check-number-status/{segment(phone)}', body=None, query={}, unwrap=False)

    async def get_contact(self, *, phone: str) -> 'ContactOut':
        """Get contact by phone."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/contacts/contact/{segment(phone)}', body=None, query={}, unwrap=False)

    async def profile(self, *, phone: str) -> 'ProfileOut':
        """Get profile."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/contacts/profile/{segment(phone)}', body=None, query={}, unwrap=False)

    async def profile_pic(self, *, phone: str) -> 'ProfilePicOut':
        """Get profile picture."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/contacts/profile-pic/{segment(phone)}', body=None, query={}, unwrap=False)

    async def profile_status(self, *, phone: str) -> 'ProfileOut':
        """Get profile status."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/contacts/profile-status/{segment(phone)}', body=None, query={}, unwrap=False)

    async def blocklist(self) -> List[str]:
        """Get block list."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/contacts/blocklist', body=None, query={}, unwrap=False)

    async def block_contact(self, *, phone: str) -> 'ActionResultOut':
        """Block contact."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/contacts/block-contact', body=None, query={'phone': phone}, unwrap=False)

    async def unblock_contact(self, *, phone: str) -> 'ActionResultOut':
        """Unblock contact."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/contacts/unblock-contact', body=None, query={'phone': phone}, unwrap=False)

    async def contact_vcard(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Send contact vCard."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/contacts/vcard', body=body, query={}, unwrap=False)

    async def get_battery_level(self) -> Dict[str, Any]:
        """Get battery level."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/contacts/battery-level', body=None, query={}, unwrap=False)

class AsyncGroupsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def list_groups(self) -> List['SimpleOut']:
        """List groups."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/groups', body=None, query={}, unwrap=False)

    async def list_group_members(self, *, group_id: str) -> List['SimpleOut']:
        """List group members."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/members', body=None, query={}, unwrap=False)

    async def common_groups(self, *, wid: str) -> List['SimpleOut']:
        """Common groups with wid."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/groups/common/{segment(wid)}', body=None, query={}, unwrap=False)

    async def group_admins(self, *, group_id: str) -> List['SimpleOut']:
        """Group admins."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/admins', body=None, query={}, unwrap=False)

    async def group_invite_link(self, *, group_id: str) -> 'SimpleOut':
        """Invite link."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/invite-link', body=None, query={}, unwrap=False)

    async def group_revoke_link(self, *, group_id: str) -> 'ActionResultOut':
        """Revoke invite link."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/revoke-link', body=None, query={}, unwrap=False)

    async def group_member_ids(self, *, group_id: str) -> List[str]:
        """Group member IDs."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/member-ids', body=None, query={}, unwrap=False)

    async def create_group(self, *, body: 'CreateGroupIn') -> 'ActionResultOut':
        """Create group."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/create', body=body, query={}, unwrap=False)

    async def leave_group(self, *, body: 'LeaveGroupIn') -> 'ActionResultOut':
        """Leave group."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/leave', body=body, query={}, unwrap=False)

    async def join_code(self, *, group_id: str) -> 'SimpleOut':
        """Get join code."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/groups/{segment(group_id)}/join-code', body=None, query={}, unwrap=False)

    async def add_participants(self, *, body: 'ParticipantsIn') -> 'ActionResultOut':
        """Add participants."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/add-participants', body=body, query={}, unwrap=False)

    async def remove_participants(self, *, body: 'ParticipantsIn') -> 'ActionResultOut':
        """Remove participants."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/remove-participants', body=body, query={}, unwrap=False)

    async def promote_participants(self, *, body: 'ParticipantsIn') -> 'ActionResultOut':
        """Promote participants."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/promote-participants', body=body, query={}, unwrap=False)

    async def demote_participants(self, *, body: 'ParticipantsIn') -> 'ActionResultOut':
        """Demote participants."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/demote-participants', body=body, query={}, unwrap=False)

    async def group_info_from_invite_link(self, *, invite_code: str) -> 'SimpleOut':
        """Group info from invite link."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/groups/info-from-invite/{segment(invite_code)}', body=None, query={}, unwrap=False)

    async def group_description(self, *, body: 'GroupDescriptionIn') -> 'ActionResultOut':
        """Set group description."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/description', body=body, query={}, unwrap=False)

    async def group_property(self, *, body: 'GroupPropertyIn') -> 'ActionResultOut':
        """Set group property."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/property', body=body, query={}, unwrap=False)

    async def group_subject(self, *, body: 'GroupSubjectIn') -> 'ActionResultOut':
        """Set group subject."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/subject', body=body, query={}, unwrap=False)

    async def messages_admins_only(self, *, body: 'MessagesAdminsOnlyIn') -> 'ActionResultOut':
        """Toggle messages only for admins."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/messages-admins-only', body=body, query={}, unwrap=False)

    async def group_picture(self, *, body: 'GroupPicIn') -> 'ActionResultOut':
        """Set group picture."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/picture', body=body, query={}, unwrap=False)

    async def change_privacy_group(self, *, body: 'ChangePrivacyGroupIn') -> 'ActionResultOut':
        """Change privacy of group."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/groups/change-privacy', body=body, query={}, unwrap=False)

class AsyncLabelsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def get_all_labels(self) -> List['SimpleOut']:
        """Get all labels."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/labels', body=None, query={}, unwrap=False)

    async def add_label(self, *, body: 'AddLabelIn') -> 'ActionResultOut':
        """Add new label."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/labels/add', body=body, query={}, unwrap=False)

    async def add_or_remove_label(self, *, body: 'AddOrRemoveLabelIn') -> 'ActionResultOut':
        """Add or remove label on chats."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/labels/add-or-remove', body=body, query={}, unwrap=False)

    async def delete_all_labels(self) -> 'ActionResultOut':
        """Delete all labels."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/labels/delete-all', body=None, query={}, unwrap=False)

    async def delete_label(self, *, label_id: str) -> 'ActionResultOut':
        """Delete label by id."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/labels/delete/{segment(label_id)}', body=None, query={}, unwrap=False)

class AsyncMediaAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def platform_from_message(self, *, message_id: str) -> 'SimpleOut':
        """Get platform from message."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/media/platform-from-message/{segment(message_id)}', body=None, query={}, unwrap=False)

    async def download_media(self, *, messageId: str) -> 'SimpleOut':
        """Download media by message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/media/download', body=None, query={'messageId': messageId}, unwrap=False)

class AsyncMessagesAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def send_text_message(self, *, body: 'MessageTextIn') -> 'ActionResultOut':
        """Send text message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/text', body=body, query={}, unwrap=False)

    async def send_image_message(self, *, body: 'MessageImageIn') -> 'ActionResultOut':
        """Send image (base64)."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/image', body=body, query={}, unwrap=False)

    async def send_link_preview(self, *, body: 'LinkPreviewIn') -> 'ActionResultOut':
        """Send link preview."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/link-preview', body=body, query={}, unwrap=False)

    async def send_location(self, *, body: 'LocationIn') -> 'ActionResultOut':
        """Send location."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/location', body=body, query={}, unwrap=False)

    async def send_file_base64(self, *, body: 'FileBase64In') -> 'ActionResultOut':
        """Send file base64."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/file-base64', body=body, query={}, unwrap=False)

    async def send_voice_base64(self, *, body: 'VoiceBase64In') -> 'ActionResultOut':
        """Send voice base64."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/voice-base64', body=body, query={}, unwrap=False)

    async def get_media_by_message(self, *, message_id: str) -> 'SimpleOut':
        """Get media by message id."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/messages/{segment(message_id)}/media', body=None, query={}, unwrap=False)

    async def edit_message(self, *, body: 'EditMessageIn') -> 'ActionResultOut':
        """Edit a message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/edit', body=body, query={}, unwrap=False)

    async def forward_messages(self, *, body: 'ForwardMessagesIn') -> 'ActionResultOut':
        """Forward messages."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/forward', body=body, query={}, unwrap=False)

    async def react_message(self, *, body: 'ReactMessageIn') -> 'ActionResultOut':
        """React to a message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/react', body=body, query={}, unwrap=False)

    async def send_reply(self, *, body: 'ReplyMessageIn') -> 'ActionResultOut':
        """Send reply message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/reply', body=body, query={}, unwrap=False)

    async def send_sticker(self, *, body: 'StickerIn') -> 'ActionResultOut':
        """Send sticker (base64)."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/sticker', body=body, query={}, unwrap=False)

    async def send_mentioned(self, *, body: 'MentionedIn') -> 'ActionResultOut':
        """Send mentioned message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/mentioned', body=body, query={}, unwrap=False)

    async def send_buttons(self, *, body: 'ButtonsIn') -> 'ActionResultOut':
        """Send buttons message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/buttons', body=body, query={}, unwrap=False)

    async def send_list_message(self, *, body: 'ListMessageIn') -> 'ActionResultOut':
        """Send list message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/list', body=body, query={}, unwrap=False)

    async def send_order_message(self, *, body: 'OrderMessageIn') -> 'ActionResultOut':
        """Send order message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/order', body=body, query={}, unwrap=False)

    async def send_poll_message(self, *, body: 'PollMessageIn') -> 'ActionResultOut':
        """Send poll message."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/poll', body=body, query={}, unwrap=False)

    async def send_status_text(self, *, body: 'SendStatusIn') -> 'ActionResultOut':
        """Send profile status text."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/messages/status', body=body, query={}, unwrap=False)

class AsyncMiscAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def get_phone_number(self) -> 'SimpleOut':
        """Get current account phone number."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/misc/get-phone-number', body=None, query={}, unwrap=False)

class AsyncPresenceAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def subscribe_presence(self, *, body: 'ChatPhoneIn') -> 'ActionResultOut':
        """Subscribe presence."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/presence/subscribe', body=body, query={}, unwrap=False)

    async def set_online_presence(self, *, body: 'ChatPhoneBoolIn') -> 'ActionResultOut':
        """Set online presence."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/presence/set-online', body=body, query={}, unwrap=False)

class AsyncProductsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def get_products(self) -> List['SimpleOut']:
        """Get products."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/products', body=None, query={}, unwrap=False)

    async def add_product(self, *, body: 'AddProductIn') -> 'ActionResultOut':
        """Add product."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products', body=body, query={}, unwrap=False)

    async def get_product_by_id(self, *, product_id: str) -> 'SimpleOut':
        """Get product by id."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/products/{segment(product_id)}', body=None, query={}, unwrap=False)

    async def edit_product(self, *, body: 'EditProductIn') -> 'ActionResultOut':
        """Edit product."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/edit', body=body, query={}, unwrap=False)

    async def delete_products(self, *, body: 'DeleteProductsIn') -> 'ActionResultOut':
        """Delete products."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/delete', body=body, query={}, unwrap=False)

    async def change_product_image(self, *, body: 'ProductImageIn') -> 'ActionResultOut':
        """Change product image."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/image', body=body, query={}, unwrap=False)

    async def add_product_image(self, *, body: 'ProductImageIn') -> 'ActionResultOut':
        """Add product image."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/image/add', body=body, query={}, unwrap=False)

    async def remove_product_image(self, *, body: 'ProductImageIn') -> 'ActionResultOut':
        """Remove product image."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/image/remove', body=body, query={}, unwrap=False)

    async def set_product_visibility(self, *, body: 'ProductVisibilityIn') -> 'ActionResultOut':
        """Set product visibility."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/visibility', body=body, query={}, unwrap=False)

    async def set_cart_enabled(self, *, body: 'SetCartEnabledIn') -> 'ActionResultOut':
        """Enable/disable cart."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/cart-enabled', body=body, query={}, unwrap=False)

    async def get_collections(self) -> List['SimpleOut']:
        """Get collections."""
        return await self._client.request('GET', f'/{segment(self._instance_id)}/products/collections', body=None, query={}, unwrap=False)

    async def create_collection(self, *, body: 'CreateCollectionIn') -> 'ActionResultOut':
        """Create collection."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/collections', body=body, query={}, unwrap=False)

    async def edit_collection(self, *, body: 'EditCollectionIn') -> 'ActionResultOut':
        """Edit collection."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/collections/edit', body=body, query={}, unwrap=False)

    async def delete_collection(self, *, body: 'DeleteCollectionIn') -> 'ActionResultOut':
        """Delete collection."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/collections/delete', body=body, query={}, unwrap=False)

    async def send_link_catalog(self) -> 'ActionResultOut':
        """Send link catalog."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/products/send-link-catalog', body=None, query={}, unwrap=False)

class AsyncSmsAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def balance(self) -> 'WalletOut':
        """Remaining wallet balance."""
        return await self._client.request('GET', f'/sms/balance', body=None, query={}, unwrap=True)

    async def senders(self) -> Dict[str, Any]:
        """Sender IDs available for sending."""
        return await self._client.request('GET', f'/sms/senders', body=None, query={}, unwrap=True)

    async def send(self, *, body: 'SmsSendIn') -> 'SmsMessageOut':
        """Send one SMS."""
        return await self._client.request('POST', f'/sms/send', body=body, query={}, unwrap=True)

    async def send_bulk(self, *, body: 'SmsBulkSendIn') -> 'SmsBulkSendOut':
        """Send the same SMS to many recipients."""
        return await self._client.request('POST', f'/sms/send-bulk', body=body, query={}, unwrap=True)

    async def status(self, *, message_x_id: str) -> 'SmsMessageOut':
        """Get the delivery status of one SMS."""
        return await self._client.request('GET', f'/sms/status/{segment(message_x_id)}', body=None, query={}, unwrap=True)

    async def opt_outs(self, *, body: 'SmsOptOutIn') -> Dict[str, Any]:
        """Unsubscribe numbers (excluded from all future sends)."""
        return await self._client.request('POST', f'/sms/opt-outs', body=body, query={}, unwrap=True)

class AsyncStoriesAPI:
    def __init__(self, client, instance_id=None):
        self._client = client
        self._instance_id = instance_id

    async def send_text_storie(self, *, body: 'MessageTextIn') -> 'ActionResultOut':
        """Send text storie."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/stories/text', body=body, query={}, unwrap=False)

    async def send_image_storie(self, *, body: 'MessageImageIn') -> 'ActionResultOut':
        """Send image storie (base64)."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/stories/image', body=body, query={}, unwrap=False)

    async def send_video_storie(self, *, body: 'MessageImageIn') -> 'ActionResultOut':
        """Send video storie (base64)."""
        return await self._client.request('POST', f'/{segment(self._instance_id)}/stories/video', body=body, query={}, unwrap=False)

class AsyncWhatsAppAPI:
    def __init__(self, client, instance_id):
        self.broadcasts = AsyncBroadcastsAPI(client, instance_id)
        self.chats = AsyncChatsAPI(client, instance_id)
        self.community = AsyncCommunityAPI(client, instance_id)
        self.contacts = AsyncContactsAPI(client, instance_id)
        self.groups = AsyncGroupsAPI(client, instance_id)
        self.labels = AsyncLabelsAPI(client, instance_id)
        self.media = AsyncMediaAPI(client, instance_id)
        self.messages = AsyncMessagesAPI(client, instance_id)
        self.misc = AsyncMiscAPI(client, instance_id)
        self.presence = AsyncPresenceAPI(client, instance_id)
        self.products = AsyncProductsAPI(client, instance_id)
        self.stories = AsyncStoriesAPI(client, instance_id)

