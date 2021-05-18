import discord
import keys
from worldbuilder import WorldBuilder

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		#for channel in client.get_all_channels():
		#	print('Channel: {0}'.format(channel))
		wb = WorldBuilder()
		wb.buildWorld()

	async def on_message(self, message):
		print('{0.guild.name}/{0.channel}/{0.author}: {0.content}'.format(message))

client = MyClient()
client.run(keys.getDiscordBotKey())