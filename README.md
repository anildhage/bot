# What You're Building

**Twitter Bot with Local LLM + Manual Approval**

## The 3-Phase Workflow

**Phase 1: Draft Generation**
- Bot uses your local LLM (Ollama) to generate engagement ideas
- Creates replies, likes, retweets as "drafts"
- Stores them in `drafts.json` file
- **No Twitter API calls happen yet** — just ideas

**Phase 2: Manual Approval**
- You review all pending drafts in CLI
- You decide which ones to approve
- You have full control — reject anything you don't like
- Only approved drafts move to next phase

**Phase 3: Execution**
- Bot posts approved drafts to Twitter
- Random 2-15 second delays between posts (mimics human behavior)
- All actions logged in `drafts.json` for auditing

## Why This Is Safe

✓ You control what gets posted (approval step)
✓ Posting happens slowly with delays (not bot-like)
✓ Full audit trail (all actions logged)
✓ Can't get banned because you're approving everything
✓ Twitter sees human-like behavior

## The Tech Stack

- **Local LLM:** Ollama (runs on your machine, free)
- **Storage:** `drafts.json` (simple JSON file)
- **API:** Twitter Graph API (via tweepy)
- **CLI:** Command-line interface (you approve via terminal)

## The Commands

```
python main.py init      → Test everything works
python main.py demo      → Generate 3 sample drafts
python main.py approve   → Review & approve drafts
python main.py execute   → Post approved drafts
python main.py status    → Show how many drafts in each status
```

## Modular Design

Built to add YouTube & Instagram later. Each platform gets its own folder, but they all share:
- Same LLM engine (your local Ollama)
- Same approval queue system
- Same CLI interface

So when you add YouTube, you just plug it in.

