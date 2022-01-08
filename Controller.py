import sqlite3
from OutputManager import OutputManager
from termcolor import colored

class Controller():

	def __init__(self, dbfile):
		self.dbfile = dbfile
		self.outputManager = OutputManager()
		self.output("init "+str(dbfile), "status")

	def connect(self):
		try:
			self.connection = sqlite3.connect("database.db")
			self.output("connected","success")
		except Exception as e:
			self.output ("error"+str(e), "fail")

	def createTable(self, name, values):
		command = "CREATE TABLE IF NOT EXISTS "+name+"("
		valuesSQL = []
		for value in values:
			valuesSQL.append(str(value+" "+values[value]))
		command+=", ".join(valuesSQL)
		command+=")"
		self.execute(command)

	def listTables(self):
		command = "SELECT name FROM sqlite_master WHERE type='table'"
		results = self.execute(command)
		for row in results:
			self.output(row[0],"status")

	def addRecord(self, name, values):
		columnsSQL = []
		valuesSQL = []
		for value in values:
			columnsSQL.append(value)
			valuesSQL.append("'"+values[value]+"'")
		command = "INSERT INTO "+name+"("+",".join(columnsSQL)+") VALUES ("+",".join(valuesSQL)+")"
		self.execute(command)

	def updateRecord(self, id, values):
		command = "UPDATE Characters SET "
		valueList = []
		for value in values:
			element=str(value)
			element+="='"
			element+=str(values[value])
			element+="'"
			valueList.append(element)
		command+= (", ".join(valueList))
		command+=" WHERE id="+str(id)
		self.execute(command)

	def getRecords(self, table):
		cursor = self.connection.cursor()
		command = "SELECT * FROM Characters"
		cursor.execute(command)
		return cursor.fetchall()

	def getHeaders(self, table):
		cursor = self.connection.cursor()
		command = "PRAGMA table_info(Characters)"
		cursor.execute(command)
		results = []
		for item in cursor.fetchall():
			results.append(item[1])
		return results

	def execute(self, command):
		cursor = self.connection.cursor()
		self.output(command, "sql")
		return cursor.execute(command)

	def commit(self):
		self.output("Commit","status")
		self.connection.commit()

	def output(self, message, type):
		self.outputManager.output(message, type)

	def StringList(self, collection):
		list = []
		for value in collection:
			array = []
			for item in value:
				array.append(str(item))
			list.append(array)
		return list


if __name__ == "__main__":
	controller = Controller("database.db")
	controller.connect()
	#headers = controller.StringList(controller.getHeaders("Characters"))
	#print (headers)
	#controller.createTable("Characters", {"id":"INTEGER PRIMARY KEY","name":"TEXT","species":"TEXT","description":"TEXT"})
	#controller.listTables()
	#controller.addRecord("Characters",{"name":"Ackbar","species":"Mon Calamari","description":"Cool Admiral"})
	#controller.getRecords("Characters")
	#controller.commit()
	controller.updateRecord("1",{"name":"Gaial Ackbar","species":"Mon Calamari","description":"Cool Admiral"})
	controller.commit()
