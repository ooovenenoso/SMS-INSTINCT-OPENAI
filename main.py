# SMS INSTINCT
# Author: ooovenenoso

import openai
import discord
import os

# Set environment variables
openai.api_key = os.environ["OPENAI_API_KEY"]
TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# Set up Discord intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.typing = True
intents.message_content = True  # Add this line to enable the message contents intent

# Create a Discord client
client = discord.Client(intents=intents)

# Create event for when user sends message with "/instinct" command"
@client.event
async def on_message(message):
    if message.content.startswith("/instinct"):
        text = message.content[9:]
        
        # Use the OpenAI API to improve the text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"Mejorar el siguiente texto para propositos de marketing en idioma español: {text}"),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Send the improved text back to the user
        await message.channel.send(response["choices"][0]["text"])

client.run(TOKEN)
