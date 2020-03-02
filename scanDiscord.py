import os
import sys
import time
import datetime
import asyncio
import discord
from discord.ext import tasks

class MyClient(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.bg_task = self.loop.create_task(self.my_background_task())

	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	async def my_background_task(self):
		await self.wait_until_ready()
		lucurisID = client.get_user() #LIST OF USER ID'S TO PING



		@tasks.loop(seconds=1.0, count=20)
		async def azuregosAlert():
			await lucurisID.send('Azuregos SPAWN !')

		@tasks.loop(seconds=1.0, count=20)
		async def kazzakAlert():
			await lucurisID.send('Kazzak SPAWN !')
			
		@client.event
		async def on_message(message):
			messageUsers = 0
			if message.content.startswith('@everyone'):		
				#SPECIFIC BOSS MESSAGES
				if message.content.find('Kaz') or message.content.find('kaz'):
					kazzakAlert.start()
				elif message.content.find('Azu') or message.content.find('azu'):
					azuregosAlert.start()
				else:
					print("Whoever just @everyone'd is a useless idiot and can't spell for shit")


client = MyClient()
client.run('') #BOT TOKEN HERE
