Copy everything below into:

```text
/Users/anildhage/Downloads/bot/docs/instagram/food-lover-instagram-tester-project.md
```

```markdown
# Food Lover Instagram API Tester — Project History and MVP Guide

**Project:** Food Lover Instagram bot  
**Status:** Tester account connected; access token generated; local integration is next.  
**Last updated:** 2026-08-28

## Project Goal

Build a local-first Instagram assistant for Food Lover that can:

- Read permitted Instagram account and media information.
- Monitor supported comments and mentions.
- Draft replies and content ideas using local Ollama.
- Require human approval before public actions.
- Execute only approved actions through Meta’s official API.
- Keep tokens, logs, drafts, and account data locally.

The MVP is a controlled assistant, not an unrestricted autonomous bot.

## What We Did

### Initial Setup

We created a Meta developer app for the Food Lover Instagram project and added the Instagram product.

The Meta app provides:

- App ID.
- App Secret.
- Instagram API configuration.
- Permissions.
- Tester roles.
- Access-token generation.
- Webhook configuration.

The App ID is:

```text
1698401361456447
```

### Callback URL

The original project notes contained this placeholder callback URL:

```text
https://example.com/auth/instagram/callback
```

This is not a real local callback.

Before using an OAuth login flow, replace it with the actual callback URL used by the local application and configure the exact same URL in Meta Developer Dashboard.

### Waiting for Verification

At an earlier stage, the Instagram app setup was waiting for Meta verification or approval.

An earlier authentication attempt returned an error similar to:

```text
Insufficient developer role
```

Because of that error, we treated Meta approval and tester authorization as blockers.

Later, the Meta Developer Dashboard showed:

```text
Ready for testing
```

This allowed us to continue with development-mode testing.

Ready for testing does not mean:

- The app has unrestricted production access.
- Every Instagram account can connect.
- Every API permission is approved.
- The app can be used for mass automation.
- App Review is complete for all features.

## Tester Accounts

The Meta App Roles page showed these Instagram tester accounts:

- `iamdhage` — Instagram Tester, accepted.
- `anil.dhage.private` — Instagram Tester, initially pending.

The account:

```text
anil.dhage.private
```

is the Food Lover Instagram account.

Facebook Developer Portal login and Instagram login are separate.

Being signed into the Facebook account used for the Meta Developer Portal does not automatically log you into the Food Lover Instagram account or accept the Instagram tester invitation.

## Food Lover API Details

Known values for the Food Lover Instagram account:

```env
INSTAGRAM_APP_ID=1698401361456447
INSTAGRAM_ACCOUNT_ID=17841431640853255
INSTAGRAM_ACCOUNT_USERNAME=anil.dhage.private
INSTAGRAM_ACCESS_TOKEN=PASTE_THE_GENERATED_TOKEN_HERE
```

The access token is secret.

Never:

- Commit it to Git.
- Paste it into chat.
- Include it in screenshots.
- Put it in public documentation.
- Share it with another person.
- Store it in frontend JavaScript.
- Add it to a GitHub repository.

## Where the Values Came From

### App ID

Find the App ID in:

```text
Meta Developer Dashboard → Your App → App Dashboard
```

The current App ID is:

```text
1698401361456447
```

### App Secret

Find the App Secret in:

```text
Meta Developer Dashboard
→ App Settings
→ Basic
→ App Secret
→ Show
```

Meta may ask for the Facebook account password before displaying it.

The App Secret must remain private.

### Instagram Account Username

The Food Lover Instagram username is:

```text
anil.dhage.private
```

It is confirmed by this Instagram profile URL:

```text
https://www.instagram.com/anil.dhage.private
```

### Instagram Account ID

The account ID appeared beneath the Instagram username in the Meta token-generation screen:

```text
17841431640853255
```

### Instagram Access Token

The access token was generated from:

```text
Meta Developer Dashboard
→ Instagram API setup
→ Generate access tokens
→ anil.dhage.private
→ Generate token
```

Copy the token and store it only in the local `.env` file or another secure secret store.

## Local `.env` Configuration

Add the following to the local bot project’s `.env` file:

```env
INSTAGRAM_APP_ID=1698401361456447
INSTAGRAM_APP_SECRET=PASTE_FROM_META_APP_SETTINGS_BASIC
INSTAGRAM_ACCOUNT_ID=17841431640853255
INSTAGRAM_ACCOUNT_USERNAME=anil.dhage.private
INSTAGRAM_ACCESS_TOKEN=PASTE_GENERATED_TOKEN_HERE

INSTAGRAM_GRAPH_BASE_URL=https://graph.instagram.com
INSTAGRAM_API_BASE_URL=https://graph.instagram.com
INSTAGRAM_TOKEN_EXCHANGE_URL=https://graph.instagram.com/access_token
INSTAGRAM_TOKEN_REFRESH_URL=https://graph.instagram.com/refresh_access_token

INSTAGRAM_SCOPE_BASIC=instagram_business_basic
INSTAGRAM_SCOPE_COMMENTS=instagram_manage_comments
INSTAGRAM_SCOPE_MESSAGES=instagram_manage_messages

INSTAGRAM_WEBHOOK_ENABLED=false
INSTAGRAM_DRY_RUN=true
```

Use the `INSTAGRAM_` prefix for every Instagram setting because this project also contains X/Twitter settings and may later contain YouTube settings.

Recommended platform naming:

```text
INSTAGRAM_...  Instagram
X_...          X/Twitter
YOUTUBE_...    YouTube later
```

## Current Project Status

The current Python project originally supports X/Twitter and Ollama configuration.

The current configuration file is:

```text
/Users/anildhage/Downloads/bot/core/config.py
```

Instagram settings still need to be added to `core/config.py`.

The current bot does not yet have a complete Instagram client.

The next implementation step is to add:

- Instagram configuration fields.
- Instagram API client.
- Read-only account check.
- Token validation.
- Error handling.
- Approval workflow integration.

## What the Tester Account Can Do

The Food Lover tester account can be used to test supported API functionality, depending on the API path, account type, permissions, and current Meta access.

Potential tester activities include:

- Test authentication and token handling.
- Confirm the Instagram account ID.
- Confirm the Instagram username.
- Retrieve permitted professional-account information.
- Retrieve permitted media and metadata.
- Test comment reading where permission is available.
- Test supported comment-reply workflows where permission is available.
- Test supported messaging workflows where permission is available.
- Test webhook delivery after an HTTPS callback is configured.
- Test webhook event normalization.
- Test local draft generation.
- Test approval and rejection workflows.
- Test structured logging.
- Test error handling.
- Test token expiration handling.
- Test token refresh handling.
- Test publishing only when the selected API path and permissions support the exact action.

Start with read-only account verification.

Do not begin with automated comments, direct messages, or publishing.

## Tester Account Limitations

The tester account is for development and controlled testing.

Important limitations include:

- The account must be a professional Instagram account.
- Supported professional account types include Creator and Business.
- Development access is restricted to accounts added through the appropriate Meta tester or app-role process.
- Each tester may need to accept the invitation through Instagram.
- Facebook login does not replace Instagram authorization when the selected flow requires Instagram login.
- Available features depend on the selected Meta API path.
- Available features depend on the account type.
- Available features depend on configured and approved permissions.
- Some permissions and features require App Review.
- A generated access token can expire.
- A generated access token can be revoked.
- Webhooks require a reachable HTTPS callback and verification process.
- Instagram rate limits still apply.
- Instagram anti-spam systems still apply.
- Instagram Community Guidelines still apply.
- Meta Platform Terms still apply.
- A tester account is not permission to scrape Instagram.
- A tester account is not permission to imitate human behavior.
- A tester account is not permission to evade rate limits.
- A tester account is not permission to use unsupported automation.
- A normal personal account is not a replacement for the professional account required by the supported API path.

A token being generated does not automatically mean that every endpoint or action is available.

Always test the specific endpoint needed by the application.

## Safe Use Rules

Use the tester account conservatively.

### API Rules

- Use Meta’s official API only.
- Do not scrape Instagram web pages.
- Do not automate browser clicks.
- Do not bypass login challenges.
- Do not bypass CAPTCHA.
- Do not bypass rate limits.
- Do not bypass account restrictions.
- Do not use unofficial private APIs.
- Do not use rotating accounts to avoid limits.
- Do not use proxy networks to avoid limits.
- Do not create fake engagement.
- Do not run follow/unfollow loops.
- Do not run bulk likes.
- Do not run bulk comments.
- Do not send unsolicited direct messages.
- Do not repeatedly send similar content.
- Do not repeatedly publish near-duplicate posts.

### Content Rules

- Use Food Lover-owned content.
- Use content supplied by the account owner.
- Use public-domain material where appropriate.
- Use properly licensed material.
- Respect copyright.
- Respect privacy.
- Do not expose private messages in logs or screenshots.
- Do not collect more data than the MVP needs.
- Do not use personal data for unrelated purposes.

### Human Approval Rules

Require explicit human approval before:

- Publishing a post.
- Publishing a reel.
- Replying to a comment.
- Sending a direct message.
- Deleting content.
- Moderating or hiding content.
- Changing account settings.
- Performing an irreversible action.

Every action should be recorded in a local audit log.

The bot should help prepare and review actions. It should not attempt to look human or evade platform detection.

## Dry-Run Mode

Keep this setting enabled during development:

```env
INSTAGRAM_DRY_RUN=true
```

Dry-run mode means the application can:

- Read data.
- Generate drafts.
- Display proposed actions.
- Validate permissions.
- Test approval logic.
- Test logging.
- Avoid making real public changes.

Change to:

```env
INSTAGRAM_DRY_RUN=false
```

only after:

- Read-only testing passes.
- Approval controls pass.
- Audit logging works.
- Error handling works.
- You intentionally want to test a real supported action.

## MVP Goal

The MVP should provide this controlled workflow:

1. Load Instagram configuration from `.env`.
2. Validate that the access token exists.
3. Validate that the account ID exists.
4. Call a basic Instagram account endpoint.
5. Display the returned username and account ID.
6. Fetch a small permitted set of media, comments, or metadata.
7. Normalize the API response.
8. Store the normalized data locally.
9. Ask Ollama to draft a reply or content idea.
10. Save the draft with `pending` status.
11. Review the draft manually.
12. Edit, approve, or reject the draft.
13. Execute only explicitly approved supported actions.
14. Record the result in an audit log.
15. Never expose the access token in logs.

## Local Architecture

```text
Instagram API
    ↓
Instagram client and token validation
    ↓
Normalized local data
    ↓
SQLite / JSON / DuckDB
    ↓
Ollama draft generation
    ↓
Human approval queue
    ↓
Official API execution
    ↓
Structured audit log
```

Suggested Instagram package structure:

```text
instagram/
  __init__.py
  client.py
  auth.py
  models.py
  permissions.py
  media.py
  comments.py
  messages.py
  webhooks.py
  safety.py
  service.py
```

Keep Instagram API calls inside the `instagram/` package.

Keep reusable functions such as the approval queue, Ollama client, logging, and configuration patterns shared across platforms.

## First Read-Only Command

The first command should be read-only:

```bash
python main.py instagram-check
```

The command should report:

- Whether Instagram configuration exists.
- Whether the token is present.
- Whether the account ID is present.
- Whether the API accepts the token.
- The returned account ID.
- The returned username.
- Available permissions when the API exposes them.
- A useful error message if the request fails.

The command must not display the full access token.

## Possible API Endpoints

Potential local application endpoints:

```text
GET  /instagram/health
GET  /instagram/account
GET  /instagram/media
POST /instagram/drafts
GET  /instagram/drafts
POST /instagram/drafts/{draft_id}/approve
POST /instagram/drafts/{draft_id}/reject
POST /instagram/drafts/{draft_id}/execute
```

Do not add real publishing until the read-only check, dry-run mode, approval controls, and audit logging pass.

## Testing Plan

### Configuration Tests

- `.env` loads correctly.
- Instagram values are read correctly.
- Missing values produce safe errors.
- Empty values are detected.
- Secrets never appear in logs.
- Instagram variables do not conflict with X/Twitter variables.

### API Tests

- Basic account request succeeds.
- Invalid token produces a useful error.
- Expired token is detected.
- Revoked token is detected.
- Permission errors are explained.
- Timeout errors are handled.
- Network failures are handled.
- API error responses are normalized.
- The full token is never printed.

### Approval Tests

- New drafts start with `pending` status.
- Pending drafts cannot execute automatically.
- Rejected drafts cannot execute.
- Only approved drafts can execute.
- Human edits are preserved.
- Dry-run mode performs no public action.
- Every action is logged.
- Failed actions are recorded.

### Content Safety Tests

- Duplicate-content checks work.
- Unsolicited messaging is blocked.
- Unsupported actions are blocked.
- Missing evidence causes abstention.
- Private data is not included in generated drafts.
- Tokens are redacted.
- Sensitive data is not written to public files.

### Webhook Tests Later

- Verify the webhook challenge.
- Validate signatures where supported.
- Store raw events safely.
- Normalize event payloads.
- Deduplicate repeated deliveries.
- Route only supported event types.
- Return safe errors.

## Moving Beyond Testing

When the MVP is working:

1. Finish read-only account tests.
2. Finish media and metadata tests.
3. Finish dry-run testing.
4. Finish approval and rejection testing.
5. Finish audit logging.
6. Finish token error handling.
7. Document the exact user value of the application.
8. Remove permissions that are not needed.
9. Add privacy and data-use documentation if required.
10. Submit required permissions and features for Meta App Review when production access is needed.
11. Switch out of development/testing mode only after the review and business requirements are complete.
12. Add authorized client accounts through the supported OAuth or onboarding flow.
13. Store separate credentials for each authorized account.
14. Give each account a clear owner and authorization record.
15. Keep Food Lover as an internal test or regression-test account.

## Production Account and Roles

A production setup should use legitimate accounts and official authorization.

For a future client account:

- The client owns or authorizes the Instagram professional account.
- The client grants the application the minimum required permissions.
- The application uses official OAuth or onboarding.
- The application never asks for the client’s Instagram password.
- The client can revoke access.
- Tokens are stored securely and separately per account.
- Account ownership and consent are documented.
- The application keeps an audit trail.
- A Facebook Page or business asset may be required for the chosen Facebook Login for Business or Instagram Graph API path.
- Production credentials are kept separate from tester credentials.

Do not reuse the Food Lover token for another account.

Do not ask clients to share passwords.

Do not create fake accounts to bypass platform rules.

## Definition of MVP Done

The MVP is complete when:

- The Food Lover token loads from `.env`.
- The App Secret is stored only locally.
- A read-only account check succeeds.
- The account ID is confirmed.
- The username is confirmed.
- At least one permitted read workflow works.
- Ollama creates a structured draft.
- Drafts can be reviewed.
- Drafts can be edited.
- Drafts can be approved.
- Drafts can be rejected.
- Dry-run mode is safe.
- Real execution requires explicit approval.
- API errors are handled.
- Token errors are handled.
- Tests cover configuration.
- Tests cover API failures.
- Tests cover approval state transitions.
- Tests cover secret redaction.
- No token is committed to Git.
- No App Secret is committed to Git.
- No private message is committed to Git.
- No unnecessary personal data is committed to Git.
- The README explains setup, limitations, safety rules, and recovery steps.

## Immediate Next Steps

1. Put the real token and App Secret only in the local `.env` file.
2. Add Instagram fields to `core/config.py`.
3. Create the `instagram/` package.
4. Implement the read-only `instagram-check` command.
5. Run the basic account request.
6. Confirm the returned username and account ID.
7. Record the API result without recording the token.
8. Add the approval queue.
9. Add Ollama draft generation.
10. Add dry-run execution.
11. Add tests.
12. Only then test one carefully approved real action.
13. Leave webhooks, multi-account onboarding, App Review, and production roles for later phases.

## Existing Documentation

The original Instagram notes are stored under:

```text
/Users/anildhage/Downloads/bot/docs/instagram/
```

Relevant existing files include:

```text
account-creations-approval-setup.md
instagram-bot-companion.md
instgram-bot-companion-guide.md
layers/business-skeleton-layer.md
layers/meta-bot-core-layer.md
```

This document consolidates the project history, tester setup, API details, limitations, safety rules, MVP plan, and future production direction.
```