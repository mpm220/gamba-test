import discord
from discord.ext import commands
from discord import app_commands


class Client(commands.Bot):
    async def on_ready(self):
        await self.tree.sync()
        print(f"logged on as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith("hello"):
            await message.channel.send(f"Hi there {message.author}")

       
intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix="!", intents=intents) 


@client.tree.command(name="hello", description="Say hello!")
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there")
