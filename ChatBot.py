import socket
import json

from command_loader import CommandsManager
#from OotCustomCommands import CustomCommands

with open('ChatBot.config') as json_file:
    data = json.load(json_file)

with open('Settings.json') as json_file:
    settings = json.load(json_file)

select_Memspace = "memory.usememorydomain(\"RDRAM\")\n"
loop_begin = "while true do \n"
loop_end = "\t emu.frameadvance()\nend"
default_Lua = "while true do \n \t emu.frameadvance()\nend"

permanent_commands = []


cm = CommandsManager(settings["commands_folder"])



def ParseGameShark(gamesharkcode):
    code_type = gamesharkcode[0:2]
    memaddress = "0x"+gamesharkcode[2:8]
    value = "0x"+gamesharkcode[9:13]
    
    return (code_type,memaddress,value)

print("Init...")

#Conectando al IRC
connection_data = ('irc.chat.twitch.tv',6667)
readbuffer = ""

server = socket.socket()
server.connect(connection_data)
server.send(bytes('PASS '+ data['TOKEN']+ '\r\n','utf-8'))
server.send(bytes('NICK '+ data['BOT_NICK']+ '\r\n','utf-8'))
server.send(bytes('JOIN '+ data['CHANNEL']+ '\r\n','utf-8'))

print("Ready")



#forParsing msgs
def parsemsg(s):
    keys = ['sender', 'type', 'target', 'message']
    return dict((key, value.lstrip(':')) for key, value in zip(keys, s.split()))

def WriteCode(addrval):
    if addrval[0] == "80":
        return "\t memory.writebyte(" + addrval[1] + "," + addrval[2] +")\n"
    if addrval[0] == "81":
        return "\t memory.write_s16_be(" + addrval[1] + "," + addrval[2] +")\n"
    else:
        return "\t memory.writebyte(" + addrval[1] + "," + addrval[2] +")\n"


def GenerateLua(addrval):
    text_file =  open(settings['commands_folder'], "w")
    luastring = select_Memspace
    luastring+= loop_begin
    luastring+= WriteCode(addrval)
    luastring+= loop_end
    text_file.write(luastring)
    return luastring



    
#Loop for listening to chat
while True:
    raw =  str(server.recv(2048))
    print(raw)
    msg = parsemsg(raw)
    #If message 
    if 'message' in msg.keys():

        sender = msg['sender'].split('!')[0][3:]
        print(sender)
        #Check if it's a command
        if msg['message'].startswith('!'):
            command = (msg['message'][1:]).split("\\")[0]
            print("Comando: " + msg['message'])
            #Is a table command
            if command in commands.keys():
                adrval = ParseGameShark(commands[command]['code'])
                print(adrval)
                GenerateLua(adrval)
            #Is a hardcoded command
            elif command in cc.commands:
                GenerateLua(cc.Command("RandomizeRupees"))
            else:
                answer = 'PRIVMSG '+data['CHANNEL']+' :Comando no valido !'+command+' @'+sender+'\r\n'
                print(answer)
                server.send(bytes(answer,'utf-8'))
        else:
            print(msg)

    elif type == 'PING':
        s.send('PONG :tmi.twitch.tv\r\n');
        s.send('PING :tmi.twitch.tv\r\n');


server.close()
