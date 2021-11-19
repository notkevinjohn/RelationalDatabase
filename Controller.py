import sqlite3

class Controller():
	def __init__(self):
		self.output("Init")

	def connect(self):
		self.output("Connect")
		self.connection = sqlite3.connect("database.db")

	def createTable(self, name, values):
		cursor = self.connection.cursor()
		command = "CREATE TABLE "+name+"("
		valuesSQL = []
		for value in values:
			valuesSQL.append(str(value+" "+values[value]))
		command+=")"
		self.output(valuesSQL)


	def output(self, message):
		print (message)


if __name__ == "__main__":
	controller = Controller()
	controller.connect()
	controller.createTable("Characters", {"Name":"TEXT"})
