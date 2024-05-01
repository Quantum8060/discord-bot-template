import discord
from discord.ext import commands
from discord.commands import slash_command
import discord.ui



class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ping", description="BotのPingを確認します。")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def ping(self, ctx: discord.Interaction):
        embed = discord.Embed(title="Ping",
                        description="`{0}ms`".format(
                          round(self.bot.latency * 1000, 2)))
        await ctx.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))