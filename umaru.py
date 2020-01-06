import os

import discord

TOKEN = os.environ['DISCORD_TOKEN']

umarucry = '<:umarucry:615726271212552203>'
emoji_id = '615726271212552203'

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

        elif client.user in message.mentions:
            emoji = client.get_emoji(emoji_id)
            try:
                await message.add_reaction(emoji)
            except Exception as error:
                await message.channel.send('<:umarucry:663799760964157451> Server owner need to give me the `Add Reactions` oermission!')

        elif message.content not in '<:umarucry:663799760964157451>':
            emoji = client.get_emoji(emoji_id)
            try:
                await message.add_reaction(emoji)
            except Exception as error:
                await message.channel.send(
                    '<:umarucry:615726271212552203> Server owner need to give me the `Add Reactions` oermission!')

client = MyClient()


@client.event
async def on_ready():
    print(f'Logged on as {client.user.name} ({client.user.id})')
    print(f'Running discord.py {discord.__version__}')
    print('----------')

client.run(TOKEN)
