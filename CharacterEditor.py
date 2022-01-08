from OutputManager import *
import PySimpleGUI as sg
from OutputManager import *


class CharacterEditor():
	def __init__ (self, data, headers, controller):
		self.data = data
		self.headers = headers
		self.controller = controller
		self.cancelEvent = "CANCEL"
		self.saveEvent = "SAVE"
		self.output = OutputManager()
		self.output.output("init CharacterEditor", "status")


	def build(self):
		layout = []
		for i in range(0, len(self.data)):
			layout.append([sg.Text(self.headers[i]), sg.Input(self.data[i])])
		layout.append([sg.Button('Cancel', key=self.cancelEvent), sg.Button('Save', key=self.saveEvent)])
		window = sg.Window("Character List View", layout)
		window.source = self
		return window

	def save(self, values):
		update = {}
		for index in values:
			if not self.headers[index] == "id":
				update[self.headers[index]] = values[index]
			else:
				id = values[index]
		self.controller.updateRecord(id, update)
		self.controller.commit()



