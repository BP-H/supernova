import discord, os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Load custom instructions and knowledge
with open("data/instructions.txt", "r", encoding="utf-8") as f:
    instructions = f.read()
with open("data/knowledge.txt", "r", encoding="utf-8") as f:
    knowledge = f.read()

system_prompt = instructions.strip() + "\n\n" + knowledge.strip()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # Prevent bot from answering itself
    if message.author == client.user:
        return

    # Simple command prefix
    if message.content.startswith("!ask "):
        user_prompt = message.content[len("!ask "):]

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        answer = response.choices[0].message.content
        await message.channel.send(answer)

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)