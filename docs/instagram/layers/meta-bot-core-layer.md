# Meta Bot Core Layer

## Purpose

This document defines Layer 1: a reusable Meta bot capability layer. The goal of this layer is to expose generic, reusable API-backed bot actions that work for Instagram professional accounts without embedding any business-specific behavior, tone, or use-case rules.[1][2]

This layer should be built first and treated as a stable capability library. Later business solutions can call these actions as a second layer instead of re-implementing Meta integration each time.[3][4]

## Design goal

Layer 1 answers one question only:

**What official Meta/Instagram actions are available, and how can they be exposed as reusable bot capabilities?**[1][2]

It should not decide why an action is used, what brand tone to apply, or which workflow should run for a specific business. Those belong in Layer 2.

## Supported account model

The official Instagram platform supports only **professional accounts**: Business and Creator accounts. Personal accounts are not supported for these API-based workflows.[3][5][6]

There are two official access paths:

- **Instagram API with Instagram Login** for Instagram professional account access.[2][1]
- **Instagram API with Facebook Login for Business** for professional accounts linked into the Meta business setup, with additional business-oriented capabilities such as hashtagged media and more business metadata workflows.[3][2][7]

## Layer 1 scope

Layer 1 should own:

- Account connection and token handling.
- Permission/scopes mapping.
- Webhook intake and event normalization.
- Generic action execution.
- Standard request/response models.
- Retries, logging, rate-limit awareness, and approval flags.
- Safety wrappers around supported actions.[1][8][9]

Layer 1 should not own:

- Brand voice.
- Use-case rules.
- Lead qualification logic.
- Food-log business logic.
- Campaign logic.
- Content strategy decisions.
- Human/business escalation policies beyond generic safety controls.

## Capability groups

### 1. Account and identity

These actions establish account-level connectivity and metadata retrieval for the connected Instagram professional account.[1][2]

Possible reusable actions:

- Connect account.
- Refresh token.
- Validate token.
- Fetch account profile.
- Fetch account metadata.
- Fetch connected asset metadata.
- Fetch permission status.
- Check publishing quota / content publishing limit.[1][3][10]

Suggested action names:

- `connect_account`
- `refresh_access_token`
- `validate_access_token`
- `get_account_profile`
- `get_account_metadata`
- `get_permission_status`
- `get_publishing_limit`

### 2. Media retrieval

The API supports reading the connected account’s media and related metadata.[2][1]

Possible reusable actions:

- List media.
- Get media by id.
- Get media caption.
- Get media permalink.
- Get media type.
- Get media timestamps.
- Get media children for carousels.
- Get media thumbnail/media URL where available.[11][1]

Suggested action names:

- `list_media`
- `get_media`
- `get_media_children`
- `get_media_permalink`
- `get_media_metadata`

### 3. Content publishing

Meta documents support for publishing single images, videos, reels, and carousel posts on behalf of Instagram professional accounts.[1][12][10]

Publishing is based on a container workflow, not a single direct post call.[10]

Possible reusable actions:

- Create media container.
- Check container readiness/status.
- Publish container.
- Publish image post.
- Publish video post.
- Publish reel.
- Publish carousel.
- Publish story, if the chosen auth path and permissions support that workflow in the implementation plan.[10][13]
- Check publish quota before execution.[3][10]

Suggested action names:

- `create_media_container`
- `get_container_status`
- `publish_media_container`
- `publish_image`
- `publish_video`
- `publish_reel`
- `publish_carousel`
- `publish_story`
- `assert_publish_quota`

Notes:

- Layer 1 should support “draft-ready payload validation” before publish.
- Layer 1 should not decide what content to publish or why.
- Publishing approval can remain a generic platform safety gate.[10][3]

### 4. Comment management

Meta documents support comment moderation and replies on media owned by the connected professional account.[1][14][10]

Possible reusable actions:

- List comments on media.
- Get comment by id.
- Create top-level comment where supported by the endpoint surface.[11][14]
- Reply to comment.
- Hide comment.
- Unhide comment.
- Delete comment.
- Count comments.
- Normalize comment webhook events.[10][13]

Suggested action names:

- `list_comments`
- `get_comment`
- `create_comment`
- `reply_to_comment`
- `hide_comment`
- `unhide_comment`
- `delete_comment`
- `count_comments`
- `normalize_comment_event`

### 5. Private replies

Meta supports private replies so a professional account can send a single private message to a user who commented on the account’s post, reel, story, or eligible media surface.[15][16][17]

Possible reusable actions:

- Send private reply to commenter.
- Check private-reply eligibility/window before sending.
- Normalize comment-to-private-reply workflow state.[16][17]

Suggested action names:

- `send_private_reply`
- `can_send_private_reply`
- `build_private_reply_context`

### 6. Messaging

Meta documents official messaging support for Instagram professional accounts, including send/receive messaging flows for users who interact with the professional account, subject to the messaging rules and windows of the platform.[2][18][19]

Possible reusable actions:

- List conversations.
- Get conversation.
- List messages in conversation.
- Send text message.
- Send attachment/message payload where supported.
- Mark or normalize inbound message events.
- Fetch user profile information from messaging context where supported.[18][19][20]

Suggested action names:

- `list_conversations`
- `get_conversation`
- `list_messages`
- `send_message`
- `send_text_message`
- `normalize_message_event`
- `get_messaging_user_profile`

Important generic rule:

- Layer 1 must preserve platform constraints such as user-initiated messaging windows and eligibility rules instead of hiding them.[11][21]

### 7. Mentions and tags

Meta documents support for identifying media where the professional account was @mentioned, and webhook notifications exist for mention activity.[2][9][10]

Possible reusable actions:

- List mentioned media.
- Get mention details.
- Normalize mention webhook payload.
- Reply to eligible mention surfaces where supported.[10][13]
- List tagged media where supported by the account/login route.[11]

Suggested action names:

- `list_mentions`
- `get_mention`
- `normalize_mention_event`
- `reply_to_mention`
- `list_tagged_media`

### 8. Hashtag discovery

Hashtag-related discovery is documented on the professional-account platform, particularly in the Facebook-linked business route and Graph API–style workflows.[3][2][22]

Possible reusable actions:

- Search hashtag id.
- Get recent/top media for hashtag where permitted.
- Normalize hashtag media metadata for downstream use.[2][22]

Suggested action names:

- `search_hashtag`
- `get_hashtag_media`
- `normalize_hashtag_media`

### 9. Insights and analytics

Meta documents account and media insights for professional accounts, including media-level performance metrics and related business analytics workflows.[1][23][10]

Possible reusable actions:

- Get account insights.
- Get media insights.
- Get reel insights.
- Get story insights within supported availability windows.[11][23]
- Normalize insights for storage/reporting.

Suggested action names:

- `get_account_insights`
- `get_media_insights`
- `get_reel_insights`
- `get_story_insights`
- `normalize_insights_payload`

### 10. Webhooks and event ingestion

A reusable bot layer should support inbound webhook processing because many useful bot behaviors begin from events rather than polling only.[9][1]

Possible reusable actions:

- Verify webhook subscription.
- Receive webhook event.
- Parse event object.
- Normalize event into platform-neutral internal event type.
- Route event to internal queue.
- Persist raw and normalized event for audit.[9][19]

Suggested action names:

- `verify_webhook`
- `ingest_webhook_event`
- `normalize_webhook_event`
- `route_webhook_event`
- `store_raw_event`
- `store_normalized_event`

## Permissions map

Layer 1 should track permissions as first-class metadata because capabilities depend on approved scopes.[10][13]

Core permissions to plan around:

| Permission | Purpose | Typical capability group |
|---|---|---|
| `instagram_content_publish` | Publish photos, videos, reels, carousels, stories where supported | Publishing [10][13] |
| `instagram_manage_comments` | Read, reply to, moderate comments; mentions-related comment handling | Comments, mentions [10][13] |
| `instagram_manage_messages` | Read and send direct messages | Messaging, private replies [10][18] |
| `instagram_manage_insights` | Read account and media analytics | Insights [10][13] |

Layer 1 should expose a capability resolver that answers: “Is this action supported for this account right now?”

Suggested action name:

- `resolve_capability`

## Generic API contract shape

Layer 1 should expose stable internal contracts independent of any one use case.

Suggested request envelope:

```json
{
  "account_id": "meta_account_ref",
  "action": "reply_to_comment",
  "payload": {},
  "options": {
    "dry_run": false,
    "requires_approval": true,
    "idempotency_key": "optional"
  }
}
```

Suggested response envelope:

```json
{
  "ok": true,
  "action": "reply_to_comment",
  "provider": "instagram",
  "provider_action": "comment_reply",
  "result": {},
  "warnings": [],
  "rate_limit": {},
  "audit_ref": "log_or_event_id"
}
```

## Suggested module structure

```text
meta_core/
  auth/
  permissions/
  webhooks/
  comments/
  messaging/
  media/
  publishing/
  insights/
  mentions/
  hashtags/
  audit/
  rate_limits/
  models/
```

For an Instagram-first implementation inside the existing bot project, the equivalent could be:

```text
platforms/instagram/
  auth.py
  permissions.py
  webhooks.py
  comments.py
  messaging.py
  media.py
  publishing.py
  insights.py
  mentions.py
  hashtags.py
  models.py
```

## Readiness checklist for Layer 1

Before Layer 2 begins, Layer 1 should be considered ready only if the following are complete:

- Account connection works for a professional account.[3][8]
- Permissions are mapped and surfaced clearly.[10][13]
- Webhook verification and ingestion are working.[9]
- Media read actions are stable.[1]
- Comment actions are stable.[14][10]
- Messaging/private reply actions are stable where enabled.[18][16]
- Publishing actions are stable with container flow support.[10][1]
- Insights retrieval is stable.[23][10]
- Capability resolution is implemented so Layer 2 can detect unsupported actions safely.[10][3]
- Logging, audit, retries, and error models are in place.[3]

## Out-of-scope for Layer 1

The following should be deferred to Layer 2 or beyond:

- Business-specific prompts.
- Lead or customer qualification logic.
- Food-log recommendations.
- Brand tone and voice.
- Growth strategy.
- Campaign scheduling strategy.
- Custom moderation rules specific to one business.
- Cross-account promotional behavior logic.

## Summary

Layer 1 should be treated as a reusable **Meta bot action library**. Its job is to wrap official Meta/Instagram capabilities into safe, normalized, reusable actions that can later be consumed by different business-specific bots and workflows.[2][1][4]