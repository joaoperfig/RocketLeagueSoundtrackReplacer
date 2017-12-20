# RocketLeagueSoundtrackReplacer

### about:
Python script to replace the soundtrack of Rocket League with a custom one

### setup:
- install ptython 3 or later
- place the contents of this folder on rocketleague\TAGame\CookedPCConsole
- convert your soundtrack to .wem (see Wwise: https://www.audiokinetic.com/download/)
- place your soundtrack on rocketleague\TAGame\CookedPCConsole\_songs
- walk to rocketleague\TAGame\CookedPCConsole on a console shell
- run "python _find_songs.py"
- input "b" to backupt current songs, wait
- input "i" to install new songs, wait
- if something goes wrong use "r" to recover backed up songs
- enjoy

#### notes:
- 42 song files will be replaced
- if your soundtrack has more files than this, some will be unused
- if your soundtrack has less files than this, some will be repeated
- the original songs have not been identified (I am lazy) and your songs will replace a random ingame song
- there might be some problems with song length
- see https://steamcommunity.com/sharedfiles/filedetails/?id=646482799 for more info
