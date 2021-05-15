import discord

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		for channel in client.get_all_channels():
			print('Channel: {0}'.format(channel))

	async def on_message(self, message):
		print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('ODM4NDg3NDA5NDU2NzA5Njcz.YI70QA.y_-fpJOk__e3BzqCp-9WIrLxENM')