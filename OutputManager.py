from termcolor import colored

class OutputManager:
	types = {
		"status":"cyan"
	}

	def output(self, message, type):
		if type in self.types:
			self.printColored(message, self.types[type])
		else:
			print (messsage)

	def printColored(self, message, color):
		print (colored(message, color))
