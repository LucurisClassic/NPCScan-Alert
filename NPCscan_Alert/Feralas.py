import sys
import discord
import asyncio
client = discord.Client()
@asyncio.coroutine
def discordReport():
	yield from client.wait_until_ready()
	counter = 0
	channel = discord.Object(id='349500178971099136')
	alertMSG = '@everyone Feralas SPAWN :dragon:'                    

	while counter <=20:
		yield from client.send_message(channel, alertMSG)
		yield from asyncio.sleep(1) # task runs every 60 seconds
		counter += 1

@client.async_event
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.loop.create_task(discordReport())
client.run('MzQ5NDgzMTQ4NTE5NjY5NzYy.DH2PJw.Hulyyag963N87Nqc3t6envSSF4w')