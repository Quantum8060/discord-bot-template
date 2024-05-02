import discord
import discord.ui
from discord import Option
import os
from discord.ext import commands
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = (True)

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = discord.Bot(intents=intents)
GUILD_IDS = [1235247721934360577]
Debug_guild = [1235247721934360577]



#起動通知
@bot.event
async def on_ready():
    print(f"Bot名:{bot.user} On ready!!")
    print("------")
    channel = await bot.fetch_channel("1235247794114134037")

    await channel.send("○○BOT起動完了")



#pingコマンド
@bot.slash_command(name="ping", description="BotのPingを確認します。")
async def ping(ctx: discord.Interaction):
  embed = discord.Embed(title="Ping",
                        description="`{0}ms`".format(
                          round(bot.latency * 1000, 2)))
  await ctx.response.send_message(embed=embed)



#コマンドテンプレート
@bot.slash_command(name="", description="")
async def xxx(ctx: discord.ApplicationContext):
   
   await ctx.respond("")



bot.run(TOKEN)