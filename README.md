# NPCScan-Alert

###### Disclaimer: My brother and I made this for private servers in 2017 while polishing off a bottle of Scotch.

### Description
  Scout.py continuously scans the Screenshots folder looking for new files added after the script's initial run time. If a new screenshot is found then Scout.py executes a command to run a second script. The second script is chosen at Scout.py's run time based on whichever argument gets passed (e.g. -Kazzak). This second script will then turn on your Discord Bot, and @everyone in a channel (3 times) based on the channel ID specified in each of the secondary scripts. A lot of this 
  
 * **Requirements**
      * Python3
      * [Unitscan](https://www.curseforge.com/wow/addons/unitscan/)
      * A Discord Bot
  
### How to Install, What to Change, How to Use
  1. Download as zip. 
  2. Extract the zip to your desired location.
  3. Edit Scout.py and change the location of the Screenshots folder if yours is different.
  4. Edit Hinterlands.py, Ashenvale.py, Azuregos.py, Feralas.py, Duskwood.py, and Kazzak.py 
      1. Line 9 with your desired channel ID. 
      2. Line 25 with your Discord Bot's token.
      3. If you do not know what these are then you should follow this guide on how to set up a [Discord Bot](https://discordpy.readthedocs.io/en/latest/discord.html).
  5.  Unitscan needs to be slightly modified for this to work. All you need to do is add "Screenshot()" at line 26 in the unitscan.lua file. My file for example: https://imgur.com/XELY4Hj
  6. Running the script:
      1. Open up Command Prompt (Start Menu and type 'cmd').
      2. Type (for example): "python3 C:\Users\lucuris\Desktop\NPCscan_Alert\scout.py -Azuregos". If you chose an irregular path like in the example you will need to edit the Scout.py file to point to the correct folder.
      3. Do not close Command Prompt as that will kill the process and nothing will happen if a boss spawns. 
  7. Get on your scouter and make sure the boss you are scouting is on your Unitscan list
      1. /unitscan Azuregos
  8. Clock in on the scouting schedule.
  9. Open up netflix, pornhub, youtube whatever and check back in every 15 or so minutes to not get auto disconnected by Blizzard.
      
      
### Command Line Usage
* python3 C:\path\to\NPCscan_Alert\scout.py -Azuregos
* python3 C:\path\to\NPCscan_Alert\scout.py -Kazzak
* python3 C:\path\to\NPCscan_Alert\scout.py -Hinterlands
* python3 C:\path\to\NPCscan_Alert\scout.py -Duskwood
* python3 C:\path\to\NPCscan_Alert\scout.py -Ashenvale
* python3 C:\path\to\NPCscan_Alert\scout.py -Feralas
