# Instagram Companion Bot Setup Guide

## Recommendation

The cleanest test setup is to create **two separate Instagram professional accounts** and only connect the test creator account to the app first.[1][2] This lets the real brand account stay untouched while the Meta app, tokens, scopes, and approval flow are validated against a safe sandbox account.[1][3]

## Project framing

This setup uses two Instagram accounts with different purposes:[1][4]

- **Account A — Creator Test Account**: the public-facing test creator/business account that simulates the real brand account and is the first account the app will authorize.[1][4]
- **Account B — Bot Companion Account**: a separate Instagram business account reserved for the companion-bot identity and future experiments.[4]

For the first milestone, only **Account A** needs to be connected to the Meta app through **Instagram API with Instagram Login**; a Facebook Page is not required for this path.[1][3][5] Account B can be created now for naming, branding, and future testing, but it does not need API authorization on day one unless it will also be tested immediately.[1][5]

## Target outcome

By the end of this setup, the following should be true:[2][3]

- Two Instagram professional accounts exist and are controlled by you.[4]
- A Meta developer app of type **Business** exists.[2]
- The Instagram product is added to the app and configured for **Instagram API with Instagram Login**.[3][5]
- The app can complete OAuth for the test creator account and obtain short-lived and long-lived access tokens.[3]
- A first successful API call such as `GET /me` works for the test creator account.[2]
- You have a written list of which permissions are enabled now and which ones will be requested later.[1][3]

## Account model

| Account | Role | Type | API status now | Public purpose |
|---|---|---|---|---|
| Account A | Creator test account | Instagram **Creator** or **Business** professional account | Must be authorized first [1][2] | Simulates the real brand account for posts, comments, DMs, and insights testing [1] |
| Account B | Companion bot account | Instagram **Business** professional account | Optional for day-one auth [4][5] | Separate helper/utility identity for future companion flows |

### Which type to choose

Use **Creator** for Account A if you want it to behave more like a personal creator brand, such as a food-content page.[4] Use **Business** for Account B because the companion account is better framed as an operational support identity rather than a personal creator voice.[4][6]

## Setup steps

### 1. Create the two Instagram accounts

Create two fresh Instagram logins with separate usernames, profile photos, bios, and email ownership you control. The easiest mental model is:

- `foodlab_test_creator` for Account A.
- `foodlab_helper_bot` for Account B.

Then switch both to **professional accounts** inside Instagram under **Account type and tools**.[4] Instagram professional accounts can be either Creator or Business, and the official API requires one of those two types.[1][4]

### 2. Decide what each account is for

Lock this down before touching APIs:

- **Account A** publishes test content and acts like the real brand account.
- **Account B** exists as a companion/support identity and should not impersonate the creator.
- Do not let Account B mass-like, mass-comment, or act like a fake audience account; that is not the safe goal for the official platform flow.[1]

### 3. Create the Meta developer app

Go to Meta for Developers and create a new app with app type **Business**.[2] Meta explicitly notes that if your current app is not a Business-type app, you need a new one for this setup.[2]

Recommended app naming:

- App name: `Instagram Companion Bot Dev`
- Environment: development only for now
- Owner email: an email you control

### 4. Add the Instagram product

Inside the app dashboard, add the **Instagram Platform** product and choose **Instagram API with Instagram Login**.[1][5] This path is the least confusing starting point because it does not require a Facebook Page connection for initial auth.[1][3][5]

### 5. Configure Business Login settings

In the app dashboard, configure **Business login settings** for Instagram.[3] You will need:

- Authorization endpoint: `https://www.instagram.com/oauth/authorize`.[3]
- Token exchange endpoint: `https://api.instagram.com/oauth/access_token`.[3]
- Long-lived token exchange endpoint: `https://graph.instagram.com/access_token`.[3]
- Refresh endpoint: `https://graph.instagram.com/refresh_access_token`.[3]

Add at least one redirect URI for local development, for example:

- `http://localhost:8000/api/instagram/oauth-callback`.[5]

If you plan to use FastAPI locally, keep one redirect URI for local testing only and avoid adding production URLs until the local flow works cleanly.[5]

### 6. Define the minimum permissions for day one

Start with the smallest useful scope set. A practical phased approach is:

| Phase | Purpose | Typical permissions |
|---|---|---|
| Phase 1 | Confirm auth and read basic account info | `instagram_business_basic` or the current equivalent basic Instagram professional scope from your dashboard [5][2] |
| Phase 2 | Read media/comments/insights as needed | Add only the read permissions needed for those surfaces [1][2] |
| Phase 3 | Publish content | `instagram_business_content_publish` or current publish scope shown in app dashboard [5][1] |
| Phase 4 | Messaging | Add messaging-related permissions only when DM testing begins [1][6] |

The practical rule is: request the minimum now, then expand later. If you later need Advanced Access, Meta App Review may be required.[2]

### 7. Authorize only the test creator account first

Use the OAuth flow with **Account A** first.[2][3] Do not connect your wife’s real account yet.

The flow is:

1. Open the Instagram authorization URL.[3]
2. Log in with **Account A**.
3. Approve the requested scopes.
4. Receive an authorization code at your redirect URI.[3]
5. Exchange the code for a short-lived token.[3]
6. Exchange the short-lived token for a long-lived token.[3]
7. Store the token securely in your local dev environment, not in source control.

After auth, make a first test call such as `GET /me` to confirm the app can retrieve the Instagram professional account user ID and username.[2]

### 8. Verify the minimum working state

Before writing bot logic, verify these checkpoints:

- Login works end to end.[2][3]
- Access token exists and is valid.[3]
- Long-lived token exchange works.[3]
- `GET /me` returns the expected Account A user identity.[2]
- The account shown by the API matches the test creator account, not the bot account.

At this point, you are ready to begin local development.

## What “ready to begin coding” means

You do **not** need every permission or app review approval before starting local development. For the first development milestone, you are ready once these are complete:[2][3]

- Business app created.[2]
- Instagram product added.[1]
- Redirect URI configured.[3][5]
- Test creator account authorized.[2]
- Basic API call succeeds.[2]

That is enough to start building:

- Local OAuth callback handling.
- Token storage and refresh logic.
- Read-only account dashboard.
- Media fetch and simple reporting.
- Later, comment, insights, publishing, and messaging modules.

## Account B planning

Account B, the bot companion account, should still be created now even if it is not the first authorized account. This gives you time to reserve the name, write a bio, choose brand tone, and decide how public or transparent the bot identity should be.

Recommended minimum setup for Account B now:

- Switch to **Business** professional account.[4]
- Add a clear bio such as “Companion account for testing discovery and support experiences.”
- Do **not** attach risky automation to it yet.
- Do **not** rely on it as a fake engagement source.

Later, you can independently authorize Account B to the same app if you want multi-account testing, provided the account owner authorizes it through the same Instagram Login flow.[1][3]

## Facebook Page decision

For the current plan, a Facebook Page is **not required** because Instagram API with Instagram Login supports professional-account access without requiring a Facebook Page connection.[1][3][5] You can add Facebook Page linkage later if you choose to migrate into the Facebook Login for Business path or want shared business tools, cross-posting, or Page-linked workflows.[7][8][9]

If you later decide to give Account B its own Facebook Page, use a one-to-one pairing instead of sharing another Page; Meta documents that professional Instagram accounts can be connected to a Facebook Page through official flows.[8][9][10]

## Practical dev checklist

### Accounts

- [ ] Create Account A test creator account.
- [ ] Convert Account A to professional (Creator or Business).[4]
- [ ] Create Account B bot companion account.
- [ ] Convert Account B to professional Business.[4]
- [ ] Record usernames, emails, and recovery methods offline.

### App

- [ ] Create Meta app with **Business** type.[2]
- [ ] Add Instagram Platform product.[1][5]
- [ ] Choose Instagram API with Instagram Login.[1][5]
- [ ] Add local redirect URI.[3][5]
- [ ] Save App ID and App Secret securely.[5]

### Authorization

- [ ] Run OAuth with Account A only.[3]
- [ ] Approve minimal scopes.
- [ ] Exchange auth code for short-lived token.[3]
- [ ] Exchange short-lived token for long-lived token.[3]
- [ ] Test `GET /me`.[2]

### Safety

- [ ] Keep the real wife account disconnected for now.
- [ ] Use local `.env` or secret manager, never Git, for tokens.
- [ ] Add logging from day one.
- [ ] Build approval gates before any public posting or DM sending.
- [ ] Add a kill switch in config before enabling risky actions.



This keeps Instagram integration separated from approval logic, storage, and future platform expansion.

## Build sequence after setup

Once the setup is complete, use this build order:

1. **OAuth + token refresh**.
2. **Read-only account identity screen**.
3. **Read media and comments**.
4. **Read insights**.
5. **Draft-only actions**.
6. **Publishing with approval gate**.
7. **Messaging with strict safety rules**.
8. **Optional second-account support for Account B**.

This order gives you a stable, demoable MVP quickly while reducing risk.

## Scope control

**Build now**

- Two professional Instagram accounts.
- Meta Business app.
- Instagram Login auth flow.
- Token exchange and refresh.
- Test creator account authorization.
- Read-only account identity and media fetch.

**Build later**

- Account B authorization.
- Insights dashboard.
- Comment assistant.
- Publishing queue.
- Messaging assistant.
- Facebook Page linkage.

**Do not build unless required**

- Mass engagement logic.
- Hidden audience-simulation behavior.
- Shared Page complexity before Instagram-only auth works.
- Production multi-tenant system.
- Public deployment before local MVP works.

This is scope creep unless it improves the core user outcome or showcase narrative. The smallest credible next milestone is: **authorize Account A successfully and prove read-only access locally**.