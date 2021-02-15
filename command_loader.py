import pandas as pd 
################################################################################################
## Format for the table of commands will be as follows:
#
#	CommandName | Cost | Code | IsParametric | Value | Enabled(bool)
#
# With: 
# 	· IsParametric can have 3 values:
#		- 0 for hardcoded value
#		- 1 for parameter input (value is not used)
#		- 2 for text parameter input (value gives the name of the table with the equivalencies)
#
#
# The loading process will be as follows:
# 	1.- Loads the commands CSV
# 	2.- Checks how many equivalency tables there are and loads them
# 	3.- Stores a dictionary with the format {commands:'array', 'eqvtable_name1':'array',...}
#################################################################################################

def ParseGameShark(gamesharkcode):
    	code_type = gamesharkcode[0:2]
    	memaddress = "0x"+gamesharkcode[2:8]
    	value = "0x"+gamesharkcode[9:13]
    
    return (code_type,memaddress,value)

def CommandCode(addrval):
    if addrval[0] == "80":
        return "\t memory.writebyte(" + addrval[1] + "," + addrval[2] +")\n"
    if addrval[0] == "81":
        return "\t memory.write_s16_be(" + addrval[1] + "," + addrval[2] +")\n"
    else:
        return "\t memory.writebyte(" + addrval[1] + "," + addrval[2] +")\n"

class CommandsManager():

	def __init__(self,commands_folder,csv_file_name="commands.csv"):
		#Loads CSV
		commands = pd.read_csv(commands_folder+csv_file_name,sep='\t',index_col=0)
		self.CommandsTable= commands
		self.Commands = commands.index.tolist()
		self.AdditionalTables = {}
		#Checks equivalencies names
		values_unique = commands['Value'].unique()
		equivalencies = []
		for value in values_unique:
			if value.isnumeric() == False:
				equivalencies.append(value)
		
		#For each equivalency table, load a csv with the same name the equivalency has
		#self.CommandDictionary
		for equiv in equivalencies:
			table = pd.read_csv(commands_folder+equiv+".csv",sep = '\t',index_col=0)
			self.AdditionalTables[equiv] = table
		#dictionary for custom commands


	#Checks if the command is Valid
	def __IsCommandValid__(self,command_string):
		splitcommand = command_string.split(' ')
		command	= splitcommand[0][1:]
		#Is it a command?
		if command in self.Commands:
			IsParametric = self.loc[command]['IsParametric']
			#Requires parameters? If no
			if  IsParametric == 0:
				if splitcommand.len() > 1:
					return -2 #-means wrong amount of parameters
				else:
					return 1
			elif IsParametric == 1:
				if splitcommand.len() > 1:
					if splitcommand[1].isnumeric():
						return 1
					else:
						return -3 #wrongparametertype
				else:
					return -2 #wrong amount of parameters
			else:
				if splitcommand.len()>1:
					if splitcommand[1].isnumeric() == False:
						#check if its the table
						if splitcommand[1] in self.AdditionalTables[self.loc[command]['Value']].index.tolist():
							return 1
						else:
							return -4 #wrong item name
					else:
						return -3 
		else:
			return -1 #-1 means command doesn't exist

	#If value is < 0 then its not a command meant to be toggled. -1 means default, -2 means activated.
	#If value is 0, then it meants is an activate once then deactivate after written on the periodic refresh
	#If value is 1, it meants is an activate once then deactivate that has to be deactivated
	#If value is 2 or 3, then it means it has to be toggled. 2 means deactivated 3 is activated

	def __ToggleCommand__(self,command_string):
		command_split = command_string.split(' ')
		command = command_split[0][1:]

		if(self.__IsCommandValid__(command_string) > 0):
			enabled = self.CommandsTable.loc[command]['Enabled']
			##If -1 change to -2 and thats it
			#if enabled == -1:
			#	self.CommandsTable.loc[command]['Enabled'] = -2
			if enabled == 0:
				self.CommandsTable.loc[command]['Enabled'] = 1
			elif enabled == 2
				self.CommandsTable.loc[command]['Enabled'] = 3
			elif enabled == 3
				self.CommandsTable.loc[command]['Enabled'] = 2	
		return -1

	

	def __GenerateLua__(self):
		select_Memspace = "memory.usememorydomain(\"RDRAM\")\n"
		loop_begin = "while true do \n"
		loop_end = "\t emu.frameadvance()\nend"
		default_Lua = "while true do \n \t emu.frameadvance()\nend"

		output_string = ""

		#Change memspace
		output_string += select_Memspace

		#First, add those commands that are a 1 and disable them (set back to 0)
		temporal = self.CommandsTable.loc['Value' == 1]



