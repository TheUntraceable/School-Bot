# Updated
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
class Status(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_connect(self):
        print(f"{self.client.user} has connected to Discord!")
    @commands.Cog.listener()
    async def on_ready(self):
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print(f'{self.client.user} is ready!')
        print(f"ID - {self.client.user.id} ")
        print(f"Connected to {len(self.client.guilds)} servers which have {len(self.client.users)} members, and message has been sent in of channels!") 
        print("-------------------------------------------------------------------------------------------------------------------------------------")
    @commands.Cog.listener()
    async def on_shard_connect(self,shard_id):
        print(f"Shard connected : {shard_id}")
    @commands.Cog.listener()
    async def on_disconnect(self):
        print(f"{self.client.user} has disconnected from Discord!")
    @commands.Cog.listener()
    async def on_shard_disconnect(self,shard_id):
        print(f"{shard_id} has disconnected from Discord!")
    @commands.Cog.listener()
    async def on_shard_ready(self, shard_id):
        print(f"Shard {shard_id} is ready!")
    @commands.Cog.listener()
    async def on_resumed(self):
        print(f"{self.client.user} has reconnected to Discord!")
    @commands.Cog.listener()
    async def on_shard_resumed(self, shard_id):
        print(f"{shard_id} has reconnected to Discord!")
    @commands.command(description="Gets the bot's current ping.")
    @commands.cooldown(1,5, BucketType.user)
    async def ping(self, ctx):
        await ctx.reply(f"Currently Active! {round(self.client.latency * 1000)}ms")
def setup(client):
    client.add_cog(Status(client))