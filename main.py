import discord
from discord import Option
import discord.ui
import os
from discord.ext import commands
from dotenv import load_dotenv
import asyncio



intents = discord.Intents.default()
intents.message_content = (True)

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = discord.Bot(intents=intents)
GUILD_IDS= [1235247721934360577]
debug_guild=[1235247721934360577]



@bot.event
async def on_ready():

   print(f"Bot名:{bot.user} On ready!!")
   print('------')
   channel = await bot.fetch_channel("1235247794114134037")

   await channel.send("〇〇BOT起動完了")

cogs_list = [
    'cogs_template',
    'ping'
]

for cog in cogs_list:
    bot.load_extension(f'Cogs.{cog}')

bot.run(TOKEN)
