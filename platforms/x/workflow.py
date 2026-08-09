from dotenv import load_dotenv
from platforms.x.client import XClient

load_dotenv()


def run_x_api_smoke_test():
    # Run a safe end-to-end X API check for auth, post, timeline, and delete.
    x_client = XClient()

    print("\n🔍 X API smoke test")
    print("=" * 40)

    me = x_client.get_me()
    user = me.data
    print(f"Authenticated as: {user.name} (@{user.username})")
    print(f"User ID: {user.id}")

    post = x_client.create_post("Testing X API from bot project. This is a temporary test post.")
    tweet_id = post.data["id"]
    print(f"Created post ID: {tweet_id}")

    recent_posts = x_client.get_user_posts(max_results=5)
    post_count = len(recent_posts.data) if recent_posts.data else 0
    print(f"Fetched recent posts: {post_count}")

    deleted = x_client.delete_post(tweet_id)
    print(f"Deleted post: {deleted.data['deleted']}")

    return {
        "user_id": user.id,
        "username": user.username,
        "created_tweet_id": tweet_id,
        "deleted": deleted.data["deleted"],
    }


if __name__ == "__main__":
    result = run_x_api_smoke_test()
    print("\n✅ X API test completed")
    print(result)
