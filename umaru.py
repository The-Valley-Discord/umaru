import os

import discord

TOKEN = os.environ['DISCORD_TOKEN']

umarucry = '<:umarucry:615726271212552203>'

class MyClient(discord.Client):
    async def on_message(self, message):
        channels = ['umaru', 'cry']
        roles = [role.name for role in message.author.roles]
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content not in umarucry and "Umaru Moderator" not in roles and message.channel.name in channels:
            print(message.created_at)
            print(message.guild)
            print(message.channel.name)
            print(message.author)
            print(message.content)
            try:
                await message.delete()
            except Exception as error:
                await message.channel.send(f'{umarucry} Server owner need to give me the `Manage Messages` permission!')
            await message.channel.send('{0} {1.author.mention}'.format(umarucry, message))
            print("---")

        elif self.user in message.mentions:
            try:
                await message.add_reaction(umarucry)
            except Exception as error:
                print(error)
                print('Failed to add reaction')
                await message.channel.send(f'{umarucry} Server owner need to give me the `Add Reactions` permission!')

        elif message.content not in umarucry:
            try:
                await message.add_reaction(umarucry)
            except Exception as error:
                print(error)
                print('Failed to add reaction')
                await message.channel.send(f'{umarucry} Server owner need to give me the `Add Reactions` permission!')

client = MyClient()


@client.event
async def on_ready():
    print(f'Logged on as {client.user.name} ({client.user.id})')
    print(f'Running discord.py {discord.__version__}')
    print('----------')

client.run(TOKEN)
