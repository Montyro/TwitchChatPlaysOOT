class CustomCommands():
	
	def __init__(self):
		self.commands = ["RandomizeRupees"]


	def Command(self, string):

		switch(string){
			case "RandomizeRupees":
				n = random.randint(0,999)
				print( "memory.write_s16_be( 0x11A604, 0x" + hex(n) +")\n")

		}
