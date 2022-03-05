import os
import emoji
import sys
import discord
from discord.ext import commands
from datetime import datetime

class Admin(commands.Cog):
    """Admin Tools"""

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(name='dream', help='Dream', hidden=True)
    @commands.is_owner()
    async def admin_stop(self, ctx):
        try:
          await ctx.send(f'Going to chase rainbows . . . ')
          print(f'Chasing rainbows')
          await ctx.bot.logout()
          os.kill(os.getppid(), 0)
        except Exception as e:
          await ctx.send(f'I did not chase rainbows for the following reason: {str(e)}')
          print(f'Failed to chase the rainbows')

    @commands.command(name='load', hidden=True)
    # @commands.is_owner()
    async def admin_cog_load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'I failed to load the cog for the following reason: {type(e).__name__} - {e}')
        else:
            await ctx.send('Loaded the cog')

    @commands.command(name='unload', hidden=True)
    # @commands.is_owner()
    async def admin_cog_unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'I failed to unload the cog for the following reason: {type(e).__name__} - {e}')
        else:
            await ctx.send('Unloaded the cog')

    @commands.command(name='reload', hidden=True)
    # @commands.is_owner()
    async def admin_cog_reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'I failed to reload the cog for the following reason: {type(e).__name__} - {e}')
        else:
            await ctx.send('Reloaded the cog')

# Loads the cog
def setup(bot):
    bot.add_cog(Admin(bot))
