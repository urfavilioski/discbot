import discord
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ['discordkey']
MENTIONED_USER_ID = '335048615603208193'
activity = discord.Activity(type=discord.ActivityType.watching, name="Galaksija 🌌")
status = discord.Status.dnd

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, status=status, activity=activity)

@bot.event

async def on_message(message):
  if MENTIONED_USER_ID in [str(user.id) for user in message.mention]:
    try:
      for i in range(50):
        await message.author.send("GET SPAMMED")
    except discord.Forbidden:
      await message.channel.send(f"{message.author.mention}, pusi kur.")
  await bot.process_commands(message)

webserver.keep_alive()
bot.run(DISCORD_TOKEN)
