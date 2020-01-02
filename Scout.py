import os
import sys
import time
import datetime
import subprocess
import asyncio
import discord
import ffmpeg
# screenshotsfolder = 'C:\\Program Files (x86)\\World of Warcraft\\_classic_\\Screenshots'
screenshotsfolder= '/Users/tim/Desktop/scannerTest'
client = discord.Client()

async def eventTrigger(unixtimestamp,filename,voicechannel):
	print ("Detected file %s @ %s" % (os.path.join(screenshotsfolder,"WoWScrnShot_"+filename+".jpg"), unixtimestamp))
	if sys.argv[1] == '-Hinterlands':
		msg='@everyone Emerald Dragon SPAWN - Hinterlands ! <:emeraldDragons:644964005823119370>'
		success = await discordReport(msg)
		voicechannel.play(discord.FFmpegPCMAudio('/Users/tim/Downloads/key_secret.mp3'))
		if success == True:
			time.sleep(120)
			sys.exit(0)
	elif sys.argv[1] == '-Ashenvale':
		msg='@everyone Emerald Dragon SPAWN - Ashenvale ! <:emeraldDragons:644964005823119370>'
		success = await discordReport(msg)
		voicechannel.play(discord.FFmpegPCMAudio('/Users/tim/Downloads/key_secret.mp3'))
		if success == True:
			time.sleep(120)
			sys.exit(0)
	elif sys.argv[1] == '-Feralas':
		msg='@everyone Emerald Dragon SPAWN - Feralas ! <:emeraldDragons:644964005823119370>'
		success = await discordReport(msg)
		voicechannel.play(discord.FFmpegPCMAudio('/Users/tim/Downloads/key_secret.mp3'))
		if success == True:
			time.sleep(120)
			sys.exit(0)
	elif sys.argv[1] == '-Duskwood':
		msg='@everyone Emerald Dragon SPAWN - Duskwood ! <:emeraldDragons:644964005823119370>'
		success = await discordReport(msg)
		voicechannel.play(discord.FFmpegPCMAudio('/Users/tim/Downloads/key_secret.mp3'))
		if success == True:
			time.sleep(120)
			sys.exit(0)
	elif sys.argv[1] == '-Kazzak':
		msg='@everyone Kazzak SPAWN - Blasted Lands ! <:kazzak:644626880816873501>'
		success = await discordReport(msg)
		voicechannel.play(discord.FFmpegPCMAudio('/Users/tim/Downloads/key_secret.mp3'))
		if success == True:
			time.sleep(120)
			sys.exit(0)
	elif sys.argv[1] == '-Azuregos':
		msg='@everyone Azuregos SPAWN - Azshara ! <:azuregos:644626896377872436>'
		success = await discordReport(msg)
		voicechannel.play(discord.FFmpegPCMAudio('/Users/tim/Downloads/key_secret.mp3'))
		if success == True:
			time.sleep(120)
			sys.exit(0)
	else:
		msg='@everyone Something SPAWNED - My owner fucked up and did not specify where!'
		success = await discordReport(msg)
		voicechannel.play(discord.FFmpegPCMAudio('/Users/tim/Downloads/key_secret.mp3'))
		if success == True:
			time.sleep(120)
			sys.exit(0)

async def discordReport(msg):
	counter = 0
	coalition = client.get_channel(349500178971099136) #not actually coalition 
	# tempest = client.get_channel(349500178971099136) #not actually tempest 
	if msg!=None:
		while counter <=2:
			await coalition.send(msg)
			# await tempest.send(msg)
			counter += 1
	return True

async def activeScanner():
	voicechannel=client.get_channel(126901181615308801)
	vc = await voicechannel.connect(timeout=1.0, reconnect=True)
	first_ran_time = time.time()
	data = {}
	try:
		while True:
			for file in os.listdir(screenshotsfolder):
				if file.startswith("WoWScrnShot_") and file.endswith(".jpg"):
					fndtstr =  file.replace("WoWScrnShot_",'').replace(".jpg",'')
					fndt = time.mktime(datetime.datetime.strptime(fndtstr, "%m%d%y_%H%M%S").timetuple())
					if fndt not in data.keys():
						if fndt > first_ran_time:
							data[fndt]=fndtstr
							msg = await eventTrigger(fndt,fndtstr,vc)
						else:
							#not from this session, ignore
							pass
					else:
						#already know about it, ignore
						pass
	except KeyboardInterrupt:
		pass

@client.event
async def on_ready():
	for guild in client.guilds:
			if guild.name == GUILD:
				break
	print(f'{client.user} is connected to the following guild:\n')
	print(f'{guild.name}(id: {guild.id})')
	msg=None
	await discordReport(msg)
	await activeScanner()

GUILD=126901181615308800
client.run('NjE0OTYyMjY2MDIxODIyNDY1.Xg4z-Q.bzM1DapCv9MS3DvGBW27DC4rL7g')
