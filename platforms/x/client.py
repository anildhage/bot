import os
import tweepy


class XClient:
    # Low-level client for authenticated X API calls.
    def __init__(self):
        self.client = None
        self.user = None

    def initialize(self):
        # Build the Tweepy client from environment variables.
        consumer_key = os.getenv("X_CONSUMER_KEY")
        consumer_secret = os.getenv("X_CONSUMER_SECRET")
        access_token = os.getenv("X_ACCESS_TOKEN")
        access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
        bearer_token = os.getenv("X_BEARER_TOKEN")

        missing = [
            key for key, value in {
                "X_CONSUMER_KEY": consumer_key,
                "X_CONSUMER_SECRET": consumer_secret,
                "X_ACCESS_TOKEN": access_token,
                "X_ACCESS_TOKEN_SECRET": access_token_secret,
                "X_BEARER_TOKEN": bearer_token,
            }.items() if not value
        ]

        if missing:
            raise ValueError(f"Missing X credentials: {', '.join(missing)}")

        self.client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True,
        )
        return self.client

    def get_me(self):
        # Verify user authentication and return the authenticated account.
        self._ensure_client()
        response = self.client.get_me(user_fields=["id", "name", "username", "public_metrics"])
        self.user = response.data
        return response

    def create_post(self, text):
        # Create a new X post for the authenticated user.
        self._ensure_client()
        if not text or not text.strip():
            raise ValueError("Post text cannot be empty.")
        return self.client.create_tweet(text=text.strip())

    def delete_post(self, tweet_id):
        # Delete an X post by post ID.
        self._ensure_client()
        if not tweet_id:
            raise ValueError("tweet_id is required.")
        return self.client.delete_tweet(tweet_id)

    def get_user_posts(self, user_id=None, max_results=5):
        # Fetch recent posts for the authenticated user or a provided user ID.
        self._ensure_client()
        target_user_id = user_id or self._get_cached_user_id()
        return self.client.get_users_tweets(
            id=target_user_id,
            max_results=max_results,
            tweet_fields=["created_at", "public_metrics", "conversation_id"],
        )

    def _get_cached_user_id(self):
        # Reuse the authenticated user ID after get_me has succeeded.
        if self.user and getattr(self.user, "id", None):
            return self.user.id
        response = self.get_me()
        return response.data.id

    def _ensure_client(self):
        # Lazily initialize the client before making API calls.
        if self.client is None:
            self.initialize()
