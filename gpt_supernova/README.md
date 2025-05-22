# GPT Discord Bot Template

## Quick Start
1. Clone the repo or unzip the download.
2. `mv .env.example .env` and paste your tokens.
3. Drop your custom instructions into `data/instructions.txt`.
4. Drop any reference knowledge into `data/knowledge.txt`.
5. `pip install -r requirements.txt`
6. `python main.py`
7. In Discord, type `!ask your question` and the bot responds with GPT-4o.

## Folder Structure
```
gpt_discord_bot/
  main.py               # Bot entry‑point
  .env.example          # Environment variables template
  requirements.txt      # Python dependencies
  data/
    instructions.txt    # Custom system instructions
    knowledge.txt       # Domain knowledge base
```