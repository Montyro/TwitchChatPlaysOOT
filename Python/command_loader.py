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

class CommandsManager():

	def __init__(self,commands_folder,csv_file_name="commands.csv"):
		#Loads CSV
		commands = pd.read_csv(commands_folder+csv_file_name)

		print(commands)
		#Checks equivalencies names

		#For each equivalency table, load a csv with the same name the equivalency has

		self.CommandDictionary = {'commands':[]}

	def __GetLuaForParameter__(self,command, parameter=None):
