# Instagram Bot Setup Documentation

## 1. Create the Instagram account

### What I did

1. I created an Instagram account named **Food Lover**.
2. I changed it to a **Creator** account.
3. I kept the account as a professional account.

### Why I did this

The Instagram API requires a professional Instagram account. Both **Creator** and **Business** accounts are supported.[1]

***

## 2. Create a Meta developer account

### What I did

1. I opened Meta for Developers:  
   [https://developers.facebook.com/](https://developers.facebook.com/)
2. I logged in with my Facebook account.
3. I registered as a Meta developer if Meta requested registration.

### Why I did this

Meta requires a developer account before creating an application for API access.[2]

***

## 3. Create the Meta app

### What I did

1. I opened the Meta app dashboard:  
   [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/)
2. I selected **Create App**.
3. I selected the **Business** app type.
4. I entered the app name and contact email.
5. I created the app.

### Why I did this

The Meta app represents the bot and provides the App ID, App Secret, API products, permissions, and authentication settings. Meta’s Instagram setup requires a Business-type app for this configuration.[3][2]

***

## 4. Find the App ID

### What I did

1. I opened the app dashboard.
2. I opened **App settings → Basic**.
3. I copied the App ID:
   ```text
   1698401361456447
   ```

### Why I did this

The App ID identifies the Meta application during the Instagram authorization process.[4]

### Security note

I did not share the App Secret. The App Secret must remain private and must not be placed in frontend code, screenshots, GitHub, or chat.

***

## 5. Add the Instagram product

### What I did

1. I opened my Meta app dashboard:  
   [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/)
2. I selected the Food Lover app.
3. I clicked **Add Product**.
4. I selected **Instagram**.
5. I selected **Instagram API with Instagram Login**.
6. I opened the Instagram API setup page.

### Why I did this

The Instagram product provides the login flow and API configuration for accessing a professional Instagram account.[5][6]

***

## 6. Configure Business Login

### What I did

1. I opened the Instagram API setup.
2. I opened **Set up Instagram Business Login**.
3. Meta asked for a redirect URL.
4. I entered:
   ```text
   http://localhost:8000/auth/instagram/callback
   ```
5. Meta returned an error when saving the localhost URL.
6. I replaced it with:
   ```text
   https://example.com/auth/instagram/callback
   ```
7. Meta accepted and saved the redirect URL.

### Why I did this

The redirect URL tells Instagram where to send the user after authorization. The redirect URL used during login must exactly match the URL saved in the Meta app.[5]

### Important

The saved redirect URL was:

```text
https://example.com/auth/instagram/callback
```

This is currently a placeholder. It is not yet a working callback endpoint.

***

## 7. Attempt the Instagram authorization

### What I did

1. I created an Instagram authorization URL using:
   - App ID:
     ```text
     1698401361456447
     ```
   - Redirect URL:
     ```text
     https://example.com/auth/instagram/callback
     ```
2. I opened the authorization URL in a browser.
3. Instagram returned:
   ```text
   Insufficient developer role
   ```

### Why I did this

This test checks whether the Instagram account is allowed to authorize the Meta app. The authorization flow normally returns a temporary code after the user approves access.[5]

### What the error meant

Meta had not yet allowed the Food Lover account to use the app. The problem was a Meta account, business portfolio, or developer-role restriction—not the App ID or redirect URL.

***

## 8. Open Meta Business Settings

### What I did

1. I opened:  
   [https://business.facebook.com/settings](https://business.facebook.com/settings)
2. I logged in with the **Facebook account** that created the Meta app.
3. I selected the **Food Lover** business portfolio.

### Why I did this

Meta Business Settings is where business assets such as Instagram accounts, Facebook Pages, people, and apps are managed.[7]

### Login rule

- I used my **Facebook login** to enter Meta Business Settings.
- I used my **Instagram login** only when Meta opened the Instagram connection window.

***

## 9. Open Instagram accounts

### What I did

1. In Business Settings, I opened **Accounts**.
2. I selected **Instagram accounts**.
3. I clicked **Add**.
4. I selected the option to claim or connect an Instagram account.

### Why I did this

Adding the account to the business portfolio gives the portfolio access to manage the professional Instagram account. Meta requires full control of the business portfolio for this action.[8]

***

## 10. Log in to Instagram

### What I did

1. Meta opened an Instagram authorization window.
2. I saw the account:
   ```text
   anil.dhage.private
   ```
3. I clicked **Log in as anil.dhage.private**.
4. Meta did not show the Food Lover account as an account available to claim.

### Why I did this

The Instagram account must be connected to the correct business portfolio before the API authorization can work. Meta also requires that the account not already belong to another business portfolio.[8]

***

## 11. Check the Instagram professional profile

### What I did

1. I opened Instagram settings.
2. I opened **Edit Profile**.
3. I checked **Profile information**.
4. I found the **Facebook** section.
5. It showed:
   ```text
   Connect
   ```

### Why I did this

The Instagram Creator account was not connected to a Facebook Page. Meta supports connecting professional Instagram accounts to Facebook Pages for business tools and account management.[9]

***

## 12. Attempt to create a Facebook Page

### What I did

1. I clicked **Connect** next to Facebook.
2. I selected **Create a Facebook Page**.
3. I entered:
   ```text
   Page name: Food Lover
   Category: Digital creator
   ```
4. I clicked **Create**.
5. Meta returned:
   ```text
   Sorry, something went wrong: There was an error while processing your request.
   ```

### Why I did this

A Facebook Page can be connected to the professional Instagram account and managed within the same business portfolio.[10][9]

### Result

The Page creation failed because the Food Lover business portfolio was restricted.

***

## 13. Discover the business portfolio restriction

### What I did

1. I opened Meta Business Support Home:  
   [https://business.facebook.com/business-support-home](https://business.facebook.com/business-support-home)
2. I selected the **Food Lover** business portfolio.
3. I opened the account overview.
4. Meta showed:
   ```text
   Business portfolio restricted from advertising
   ```

### Why I did this

The business portfolio restriction was preventing advertising and may also have been interfering with creating or connecting business assets. Meta provides Business Support Home for checking restrictions and requesting reviews.[11][12]

### Important

The restriction was related to Meta business/advertising access. It was not proof that the Instagram Creator account itself was deleted or unusable.

***

## 14. Request a review

### What I did

1. In Business Support Home, I selected the restricted **Food Lover** business portfolio.
2. I clicked **Request review**.
3. Meta requested identity verification.
4. I uploaded an official government ID.
5. Meta accepted the review request.
6. The status changed to:
   ```text
   In review
   ```
7. Meta displayed:
   ```text
   You’ll hear back from us within 4 days
   ```

### Why I did this

Meta requires identity verification to confirm that the business portfolio belongs to the person requesting access. The review is required before Meta can remove or change the restriction.[13][14]

### Current status

The review is pending.

I should not:

- Upload the ID again.
- Submit another review.
- Create another business portfolio.
- Keep retrying the Instagram connection.
- Share the ID image publicly.
- Share the App Secret or access token.

***

# What I Can Complete During Review

## 1. Create the local project

I can create the bot project structure:

```text
instagram-bot/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   │   └── instagram_auth.py
│   └── services/
│       └── instagram_api.py
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## 2. Create the FastAPI server

I can create a local FastAPI application with:

```text
GET /health
GET /auth/instagram/login
GET /auth/instagram/callback
```

The callback route can initially return a test message instead of exchanging a real Instagram code.

## 3. Configure environment variables

I can create `.env.example`:

```env
INSTAGRAM_APP_ID=1698401361456447
INSTAGRAM_APP_SECRET=replace_later
INSTAGRAM_REDIRECT_URI=https://example.com/auth/instagram/callback
```

I should keep the real `.env` file private and excluded from Git.

## 4. Implement the OAuth URL builder

I can implement code that creates the Instagram authorization URL using:

- App ID.
- Redirect URI.
- Response type.
- Requested permissions.

The login URL can be tested structurally without completing Meta authorization.

## 5. Implement token-exchange code

I can write the code for the documented endpoints:

```text
https://api.instagram.com/oauth/access_token
https://graph.instagram.com/access_token
https://graph.instagram.com/refresh_access_token
```

These endpoints are used to exchange an authorization code, obtain a long-lived token, and refresh a token.[5]

I must not test with a real token until Meta approves the business portfolio.

## 6. Write automated tests

I can test:

- Redirect URL encoding.
- Authorization URL generation.
- Missing environment variables.
- Invalid callback parameters.
- OAuth error responses.
- Token-exchange request formatting.
- Safe handling of secrets.
- API timeout and error handling.

## 7. Create mock API responses

I can create local mock responses for:

```json
{
  "user_id": "mock-user-id",
  "username": "food_lover"
}
```

Meta’s basic API flow uses the `/me` endpoint to retrieve the Instagram user ID and username.[3]

## 8. Prepare the bot features

I can build the code for:

- Reading the Instagram profile.
- Reading media metadata.
- Listing posts.
- Preparing captions.
- Preparing hashtags.
- Creating a review queue.
- Requiring manual approval before publishing.
- Logging API requests without logging secrets.

## 9. Prepare documentation

I can document:

- OAuth flow.
- Required permissions.
- Environment variables.
- Local callback behavior.
- Token storage rules.
- API error handling.
- Manual approval requirements.
- Development and testing commands.

## 10. Wait for Meta approval

After Meta completes the review:

1. Check:  
   [https://business.facebook.com/business-support-home](https://business.facebook.com/business-support-home)
2. Confirm whether the Food Lover portfolio restriction is removed.
3. Return to:  
   [https://business.facebook.com/settings](https://business.facebook.com/settings)
4. Connect the Food Lover Instagram account.
5. Return to:  
   [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/)
6. Retry the Instagram authorization flow.
7. Test the callback.
8. Exchange the returned code for an access token.
9. Call the Instagram `/me` endpoint.
10. Store the token securely.
