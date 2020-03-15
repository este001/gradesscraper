import os
import discord
from dotenv import load_dotenv


def doit(*args):
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    client = discord.Client()

    @client.event
    async def on_ready():
        # for guild in client.guilds:
        #     if guild.name == GUILD:
        #         break
        # print(
        #     f'{client.user} is connected to the following guild:\n'
        #     f'{guild.name}(id: {guild.id})\n'
        #     f'{client.guilds[0]} hallå'
        # )

        if not all(args):
            channel = client.get_channel(688709593584631831)
            await channel.send('Grades are set')
        else:
            channel = client.get_channel(688709593584631831)
            await channel.send(args[0])

    client.run(TOKEN)

if __name__ == '__main__':
    doit()



