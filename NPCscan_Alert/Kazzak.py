import sys
import discord
import asyncio
client = discord.Client()
@asyncio.coroutine
def discordReport():
	yield from client.wait_until_ready()
	counter = 0
	channel = discord.Object(id='') #YOUR DESIRED CHANNEL ID!!!!!!!!!!!!!!!!!!!!
	alertMSG = '@everyone Lord Kazzak SPAWN - Blasted Lands ! :Kazzak:'

	while True:
		if counter <=3:
			yield from client.send_message(channel, alertMSG)
			yield from asyncio.sleep(1) # task runs every 60 seconds
			counter += 1
		else:
			pass
@client.async_event
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.loop.create_task(discordReport())
client.run('')# YOUR BOT'S TOKEN HERE
