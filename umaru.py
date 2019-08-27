import os

import discord
from discord.utils import get

TOKEN = os.environ['DISCORD_TOKEN']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        emotes = ['<:umarucry:615726271212552203>', '<:umarucry:615064355360473088>', '<:GWnonexUmaruCry:402867193475366933>', '<:umaruMagikCry:615316023435984906>', '<:GWnonexUmaruCry:615064355360473088>']
        channels = ['umaru', 'cry']
        roles = [role.name for role in message.author.roles]
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content not in emotes and "Umaru Moderator" not in roles and message.channel.name in channels:
            print(message.created_at)
            print(message.guild)
            print(message.channel.name)
            print(message.author)
            print(message.content)
            try:
                await message.delete()
            except Exception as error:
                message.channel.send('<:umarucry:615726271212552203> Server owner need to give me the `Manage Messages` permission!')
            await message.channel.send('<:umarucry:615726271212552203> {0.author.mention}'.format(message))
            print("---")

        if client.user in message.mentions:
            emoji = client.get_emoji(615726271212552203)
            try:
                await message.add_reaction(emoji)
            except Exception as error:
                message.channel.send('<:umarucry:615726271212552203> Server owner need to give me the `Add Reactions` oermission!')

client = MyClient()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------')

client.run(TOKEN)
