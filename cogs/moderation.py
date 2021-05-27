import asyncio
import discord
import time
from discord.ext import commands
from discord import Embed, Color
from typing import Optional
from pathlib import Path

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx, amount=1): 
        amount = amount + 1
        await ctx.channel.purge(limit=amount)
        if amount-1 == 1:
         embed=discord.Embed(title="Deleted!", description=f"{amount-1} Message Was Deleted By {ctx.author.mention}", color=ctx.author.color)
         embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
         await ctx.send(embed=embed)
        elif amount-1 > 1:
         embed=discord.Embed(title="Deleted!", description=f"{amount-1} Messages Were Deleted By {ctx.message.author}", color=ctx.author.color)
         embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
         await ctx.send(embed=embed)

    @commands.command(name="ban", aliases=['ban_user', 'delete_user'])
    @commands.has_permissions(administrator=True)
    async def ban_command(self, ctx, user : discord.Member, *, reason):
        await user.ban(reason=reason)

        embed = Embed(color=discord.Color.red())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.message.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"BAN CASE | BY {ctx.author}",
                        value=f"The user {user.mention} has been banned from the guild.\nREASON: **{reason}**\nMODERATOR: {ctx.author.mention}")

        await ctx.send(embed=embed)

    @commands.command(name="kick", aliases=['kick_user'])
    @commands.has_permissions(administrator=True)
    async def kick_command(self, ctx, user : discord.Member, *, reason):
        await user.kick(reason=reason)

        embed = Embed(color=discord.Color.red())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.message.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"KICK CASE | BY {ctx.author}",
                        value=f"The user {user.mention} has been kicked from the guild.\nREASON: **{reason}**\nMODERATOR: {ctx.author.mention}")

        await ctx.send(embed=embed)

    @commands.command(name="warn", aliases=['sudo'])
    @commands.has_permissions(administrator=True)
    async def warn_command(self, ctx, user : discord.Member, *, reason):
        embed = Embed(color=discord.Color.gold())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"Warning",
                        value=f"{user.mention} you got a warning in the guild from {ctx.author.mention} for the following reason:\n**{reason}**.\nPlease stop doing wrong!")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
