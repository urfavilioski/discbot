import discord
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ['discordkey']
MENTIONED_USER_ID = '951184062331109426'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
  if MENTIONED_USER_ID in [str(user.id) for user in message.mention]:
    try:
      for i in range(50):
        await message.author.send("GET SPAMMED")
    except discord.Forbidden:
      await message.channel.send(f"{message.author.mention}, pusi kur.")
  await bot.process_commands(message)

webserver.keepalive()
bot.run(DISCORD_TOKEN)
