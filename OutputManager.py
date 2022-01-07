from termcolor import colored
import time

class OutputManager:
	types = {
		"status":"cyan",
		"success":"green",
		"sql":"magenta"
	}

	def output(self, message, type):
		header = self.header(type)
		message = header+message
		if type in self.types:
			self.printColored(message, self.types[type])
		else:
			print (message)

	def header(self, type):
		now = int(time.time())
		header = "["+str(now)+":"+str(type)+"] "
		return header

	def printColored(self, message, color):
		print (colored(message, color))
