import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(guild):
     for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed=discord.Embed(title="Hey You!", description="Use `#help` As A Guide To Know More About Me! \n I Have Many Functions Such As Games, Websites And Fun!", color=discord.Color.red())
            await channel.send(embed=embed)
        break

def setup(client):
    client.add_cog(Welcome(client))