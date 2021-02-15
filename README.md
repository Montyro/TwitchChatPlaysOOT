# ChatPlaysOOT
This is an alternative for "Crowd Control", based on text commands, that makes use of some GameShark codes and memory writting. 

<center>
  <img src="https://github.com/Montyro/TwitchChatPlaysOOT/blob/main/Images/oot.gif" width="350" height="200" />
</center>

## Schematic
<center>
  <img src="https://github.com/Montyro/TwitchChatPlaysOOT/blob/main/Images/diagram.png"  height="150" />
</center>

The emulator is listening the Lua file for modifications. This LUA file contains the gameshark code injections for the game, and is modified by the python bot when a new command is received. The bot is listening to the twitch chat (which is actually an IRC channel).

The gameshark codes are inside Commands/OcarinaOfTime.

## Current State
As of now, it works with simple commands to give items, and can enable some funny codes like getting a heart gets you killed.

## How to use
* First create your bot and get your twitch api key and fill the ChatBot.config file with your data.
* Now run ChatBot.py.
* To make it work, download bizhawk emulator, run OOT game on it and open the injector.lua in the script injection section in cheats, and check autoreload. 

## TO-DO
### Clean redundant / unsused files.
When I finally get back to working on this this will be the first thing to work on...

### User system
* [ ] A point system for chat users, so people can only use commands using accumulated points.
* [ ] Bans, VIP status.

### Command Manager
* [ ] UI that allows you to quickly create and modify command tables.

### Save Manager
* [ ] Allow the app to store the last status before close up.








