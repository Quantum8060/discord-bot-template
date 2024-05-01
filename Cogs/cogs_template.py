import discord
from discord.ext import commands
from discord.commands import slash_command # 追加



class cogs_template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="", description="") # 変更
    async def cogs_template(
            self,
            ctx: discord.ApplicationContext):
        await ctx.respond('hi!')

def setup(bot):
    bot.add_cog(cogs_template(bot))