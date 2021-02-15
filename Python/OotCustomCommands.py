import random
class CustomCommands():
	
	def __init__(self):
		self.commands = ["RandomizeRupees"]


	def Command(self, string):

		if string == "RandomizeRupees":
				
				n = random.randint(0,99)
				print("Random Rupees:",n)
				return ("81","0x11A604",""+hex(n))
				#print( "memory.write_s16_be( , 0x" + hex(n) +")\n")
				

		
