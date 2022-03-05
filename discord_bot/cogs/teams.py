#!/usr/bin/python
import discord
from discord.ext import commands
import aiohttp
import asyncio
from io import BytesIO
import psycopg2
import emoji
import os
DB_NAME = os.getenv('PSQL_DBNAME')
USER_NAME = os.getenv('PSQL_USERNAME')
PASSWORD = os.getenv('PSQL_PASSWORD')

class Teams(commands.Cog):
    '''Team Management Tools'''

    def __init__(self, bot):
        self.bot = bot

    # Events and help command
    @commands.command(name='jointeam',help='JoinTeam')
    async def jointeam(self, ctx, *args):
      conn = psycopg2.connect(database = DB_NAME, user = USER_NAME, password = PASSWORD, host = "127.0.0.1", port = "5432")

      cur = conn.cursor()

      name = args[0]
      print(name)
      try:
        cur.execute("SELECT users.id, uname, playing_for, discord_role_id from users inner join teams on users.playing_for = teams.id where uname like %s",[name])
        row = cur.fetchone()
        if row[3] is not None and row[2] != -1:
           await ctx.author.add_roles(discord.utils.get(ctx.guild.roles, id=int(row[3])))
           cur.execute("UPDATE users SET discord_id = {} where id = {}".format(ctx.author.id, row[0]))
           conn.commit()
           await ctx.message.add_reaction(emoji.emojize(':thumbs_up:'))
        elif row[2] == -1:
           await ctx.send("Hmm, {}, you don't appear to have a team yet.".format(row[2]))
        else:
           await ctx.send("Hmm, no user found. Try making an account on collegefootballrisk.com/ or try a different spelling.")
      except:
        await ctx.send("Hmm, no user found or user does not yet have a team.")
      conn.close()

    @commands.command(name='doteammake',help='doteammake')
    @commands.has_permissions(administrator=True)
    async def dbahxx(self, ctx, *args):
      conn = psycopg2.connect(database = DB_NAME, user = USER_NAME, password = PASSWORD, host = "127.0.0.1", port = "5432")

      cur = conn.cursor()
      try:
        cur.execute("SELECT tname, tshortname, id from teams")
        teams = cur.fetchall()
        for team in teams:
            existing_channel = discord.utils.get(ctx.guild.channels, name=team[0])
            if existing_channel is not None:
                if existing_channel.category is None:
                    await existing_channel.delete()
            existing_role = discord.utils.get(ctx.guild.roles, name=team[0])

            if existing_role is not None:
                print("Deleting old role {}".format(existing_role.id))
                await existing_role.delete()

            role = await ctx.guild.create_role(name=team[0])
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                role: discord.PermissionOverwrite(read_messages=True)
            }
            await ctx.guild.create_text_channel(team[1], overwrites=overwrites, category = ctx.channel.category)
            cur.execute("update teams set discord_role_id = {} where id = {}".format(role.id, team[2]))
            print("update teams set discord_role_id = {} where id = {};".format(role.id, team[2]))
        conn.commit()
        cur.close()
      except (Exception, psycopg2.DatabaseError) as error:
          print(error)

    @commands.command(name='doteamclose',help='doteammake')
    @commands.has_permissions(administrator=True)
    async def dbahxxy(self, ctx, *args):
      try:
          channels = ctx.channel.category.text_channels
          for channel in channels:
              await channel.send("Note: this channel will be deleted this weekend. Please save any resources you wish to keep before the end of the day.")
      except (Exception) as error:
          print(error)

    @commands.command(name='doteampermsclose',help='doteammake')
    @commands.has_permissions(administrator=True)
    async def dbahxxy(self, ctx, *args):
      try:
          channels = ctx.channel.category.text_channels
          for channel in channels:
              await channel.edit(sync_permissions=True)
              await channel.send("Note: this channel's settings are now synced")
      except (Exception) as error:
          print(error)

# Loads the cog
def setup(bot):
    bot.add_cog(Teams(bot))
