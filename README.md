# NPCScan-Alert

### Description
  Scout.py continuously scans the Screenshots folder looking for new files added after the script's initial run time. If a new screenshot is found then Scout.py executes a command to run a second script. The second script is chosen at Scout.py's run time based on whichever argument gets passed (e.g. -Kazzak). This second script will then turn on your Discord Bot, and @everyone in a channel (3 times) based on the channel ID specified in each of the secondary scripts. A lot of this 
  
 * **Requirements**
      * Python3
      * [Unitscan](https://www.curseforge.com/wow/addons/unitscan/)
  
### How to Install, What to Change, How to Use
  1. Download as zip. 
  2. Extract the zip to your desired location.
  3. Edit the Scout.py and change the location of the Screenshots folder if yours is different.
  4. Edit Hinterlands.py, Ashenvale.py, Azuregos.py, Feralas.py, Duskwood.py, and Kazzak.py on line 9 and line 25 with the correct information for your channel ID and bot token (respectively). If you do not know what these are then you should follow this guide on how to set up a [Discord Bot](https://discordpy.readthedocs.io/en/latest/discord.html).
  5.  Unitscan needs to be slightly modified for this to work. All you need to do is add "Screenshot()" at line 26 in the unitscan.lua file. My file for example: https://imgur.com/XELY4Hj
  6. Running the script:
      1. Open up Command Prompt (Start Menu and type 'cmd').
      2. Type (for example): "python3 C:\Users\lucuris\Desktop\NPCscan_Alert\scout.py -Azuregos". If you chose an irregular path like in the example you will need to edit the Scout.py file to point to the correct folder.
      3. Do not close Command Prompt as that will kill the process and nothing will happen if a boss spawns. 
      
      
### Acceptable Usage
* python3 C:\path\to\NPCscan_Alert\scout.py -Azuregos
* python3 C:\path\to\NPCscan_Alert\scout.py -Kazzak
* python3 C:\path\to\NPCscan_Alert\scout.py -Hinterlands
* python3 C:\path\to\NPCscan_Alert\scout.py -Duskwood
* python3 C:\path\to\NPCscan_Alert\scout.py -Ashenvale
* python3 C:\path\to\NPCscan_Alert\scout.py -Feralas
