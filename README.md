# NPCScan-Alert

###### Disclaimer: Still waiting/praying that hacks@blizzard.com will reply to my email on whether this is against EULA or not.

### Description
  Scout.py continuously scans the WoW Screenshots folder looking for new files added after the script's initial run time. If a new screenshot is found then Scout.py will then @everyone in a channel (3 times) based on the channel ID specified in each of the secondary scripts and play a song in a voice channel. 
  
 * **Requirements**
      * Python3
        * Pip
          * pip install discord
          * pip install pynacl
          * pip install ffmpeg
      * [Unitscan](https://www.curseforge.com/wow/addons/unitscan/)
      * A Discord Bot
      * FFmpeg (not just the python library)      
  
### How to Install, What to Change, How to Use
  1. Save scout.py to your desired folder. 
  2. Edit scout.py to add/change:
      1. Line 23 & line 45 with the correct path to your WoW Screenshots folder.
      2. Line 28 with the path to the song you want played.
      3. Line 35 & line 36 with the Text Channel IDs that you want ping'd.
      4. Line 65 & line 66 with the Voice Channel IDs that you want the music to play in
  3.  Unitscan needs to be slightly modified for this to work. All you need to do is add "Screenshot()" at line 26 in the unitscan.lua file. My file for example: https://imgur.com/XELY4Hj
  4. Scouting
      1. `/unitscan Azuregos`
      2. Run the Script via CMD. Examples below.

### Command Line Usage
* python C:\path\to\NPCscan_Alert\scout.py Azuregos
* python C:\path\to\NPCscan_Alert\scout.py Kazzak
* python C:\path\to\NPCscan_Alert\scout.py Hinterlands
* python C:\path\to\NPCscan_Alert\scout.py Duskwood
* python C:\path\to\NPCscan_Alert\scout.py Ashenvale
* python C:\path\to\NPCscan_Alert\scout.py Feralas
