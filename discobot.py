import os
import discord
import time
from dotenv import load_dotenv


def doit():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()

    @client.event
    async def on_ready():
        print("test")
        channel = client.get_channel(688709593584631831)
        await channel.send('Yoyoyo grades are set mother truckers')
        os._exit(0)

    client.run(TOKEN)

doit()
