import sys
import discord
import asyncio
client = discord.Client()

async def discordReport():
	await client.wait_until_ready()
	counter = 0
	channel = client.get_channel() #place desired channel ID here as an integer

	while counter <=2:
		await channel.send('@everyone Kazzak SPAWN - Blasted Lands !')
		counter += 1

# @client.async_event
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.loop.create_task(discordReport())
client.run('') #place discord bot's token here
