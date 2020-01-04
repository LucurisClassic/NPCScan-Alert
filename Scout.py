import os
import sys
import time
import datetime
import asyncio
import discord
import ffmpeg

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
		async def eventTrigger(self,unixtimestamp,filename,voicechannel):
			screenshotsfolder = 'C:\\Program Files (x86)\\World of Warcraft\\_classic_\\Screenshots'
			print ("Detected file %s @ %s" % (os.path.join(screenshotsfolder,"WoWScrnShot_"+filename+".jpg"), unixtimestamp))
			msg='@everyone %s SPAWN ! ' % sys.argv[1]
			success = await discordReport(self,msg)
			success=True
			voicechannel.play(discord.FFmpegPCMAudio('C:\\Users\\timot\\Desktop\\newScan_Alert\\Brain_Power.mp3'))
			time.sleep(300)
			await voicechannel.disconnect()
			sys.exit()
			
		async def discordReport(self,msg):
			counter = 0
			coalition = client.get_channel() #text channel ID here
			# whatheflux = client.get_channel()
			while counter <=2:
				await coalition.send(msg)
				# await whatheflux.send(msg)
				counter += 1
			return True

		async def activeScanner(self,voicechannel):
			vc = await voicechannel.connect(reconnect=True)
			screenshotsfolder = 'C:\\Program Files (x86)\\World of Warcraft\\_classic_\\Screenshots'			
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
									msg = await eventTrigger(self,fndt,fndtstr,vc)
								else:	
									pass #not from this session, ignore
							else:
								pass #already know about it, ignore
			except KeyboardInterrupt:
				pass
		voicechannel=client.get_channel()  # COALITION Voice Channel ID
		# voicechannel=client.get_channel()# WHATHEFLUX DISCORD
		await activeScanner(self,voicechannel)

client = MyClient()
client.run('') #BOT TOKEN HERE
