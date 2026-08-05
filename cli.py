import argparse, os, sys
from dotenv import load_dotenv
from core.llm_engine import OllamaEngine
from core.approval_queue import ApprovalQueue
from platforms.twitter.actions import TwitterBot

load_dotenv()

def show_banner():
    print("\n╔════════════════════════════════════════╗\n║     Twitter Bot - Approval System      ║\n║  Local LLM + Modular Architecture     ║\n╚════════════════════════════════════════╝\n")

def cmd_status(bot, queue):
    print("\n📊 Bot Status\n" + "="*40)
    pending = queue.get_pending()
    approved = queue.get_approved()
    posted = [d for d in queue.drafts.values() if d.status == "posted"]
    print(f"Pending:  {len(pending)}\nApproved: {len(approved)}\nPosted:   {len(posted)}\n")

def cmd_approve(bot, queue):
    pending = queue.get_pending()
    if not pending:
        print("✓ No pending drafts.")
        return
    print(f"\n📋 Pending Drafts ({len(pending)})\n" + "="*40)
    for draft in pending:
        print(f"\n[{draft.id}] {draft.action_type.upper()}")
        if draft.content:
            print(f"  Content: {draft.content}")
    user_input = input("\nEnter IDs to approve (comma-separated): ").strip()
    if user_input:
        try:
            approved_ids = [int(x.strip()) for x in user_input.split(",")]
            queue.approve(approved_ids)
            print(f"✓ Approved {len(approved_ids)} draft(s).")
        except:
            print("✗ Invalid input.")

def cmd_execute(bot, queue):
    approved = queue.get_approved()
    if not approved:
        print("✓ No approved drafts.")
        return
    confirm = input(f"\nExecute {len(approved)} draft(s)? (yes/no): ").strip().lower()
    if confirm == "yes":
        bot.execute_approved_drafts()

def cmd_demo(bot, queue):
    print("\n🎬 Generating demo drafts...\n")
    bot.draft_reply("demo-1", "Just shipped a new feature!")
    bot.draft_reply("demo-2", "What's your favorite Python library?")
    bot.draft_like("demo-like-1")
    print("\n✓ Demo drafts created.")

def main():
    parser = argparse.ArgumentParser(description="Twitter Bot CLI")
    parser.add_argument("command", choices=["status", "approve", "execute", "demo", "init"], help="Command to run")
    args = parser.parse_args()
    show_banner()
    llm = OllamaEngine()
    queue = ApprovalQueue()
    bot = TwitterBot(llm, queue)
    if args.command == "status":
        if not bot.initialize(): return
        cmd_status(bot, queue)
    elif args.command == "approve":
        if not bot.initialize(): return
        cmd_approve(bot, queue)
    elif args.command == "execute":
        if not bot.initialize(): return
        cmd_execute(bot, queue)
    elif args.command == "demo":
        cmd_demo(bot, queue)
    elif args.command == "init":
        print("\n🔍 Checking setup...")
        if bot.initialize():
            print("\n✓ All systems ready!")
        else:
            print("\n✗ Setup incomplete.")

if __name__ == "__main__":
    main()
