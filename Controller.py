import sqlite3
from OutputManager import OutputManager
from termcolor import colored

class Controller():
	def __init__(self, dbfile):
		self.dbfile = dbfile
		self.outputManager = OutputManager()
		self.output("Init "+str(dbfile), "status")


	def connect(self):
		self.output("Connect")
		try:
			self.connection = sqlite3.connect("database.db")
		except Error as e:
			self.output ("error"+str(e))

	def createTable(self, name, values):
		command = "CREATE TABLE IF NOT EXISTS "+name+"("
		valuesSQL = []
		for value in values:
			valuesSQL.append(str(value+" "+values[value]))
		command+=", ".join(valuesSQL)
		command+=")"
		self.execute(command)

	def listTables(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
		print (cursor.fetchall())

	def addRecord(self, name, values):
		columnsSQL = []
		valuesSQL = []
		for value in values:
			columnsSQL.append(value)
			valuesSQL.append("'"+values[value]+"'")
		command = "INSERT INTO "+name+"("+",".join(columnsSQL)+") VALUES ("+",".join(valuesSQL)+")"
		self.execute(command)

	def getRecords(self, table):
		cursor = self.connection.cursor()
		command = "SELECT * FROM Characters"
		cursor.execute(command)
		print (cursor.fetchall())

	def execute(self, command):
		cursor = self.connection.cursor()
		self.output(command)
		cursor.execute(command)

	def commit(self):
		self.connection.commit()

	def output(self, message, type):
		self.outputManager.output(message, type)


if __name__ == "__main__":
	controller = Controller("database.db")
	#controller.connect()
	#controller.createTable("Characters", {"id":"INTEGER PRIMARY KEY","name":"TEXT","species":"TEXT","description":"TEXT"})
	#controller.listTables()
	#controller.addRecord("Characters",{"name":"Ackbar","species":"Mon Calamari","description":"Cool Admiral"})
	#controller.commit()
	#controller.getRecords("Characters")
