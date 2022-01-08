import PySimpleGUI as sg
from Controller import *
from CharacterEditor import *
from OutputManager import *

class CharacterListView():
	def __init__(self, controller):
		self.controller = controller
		self.output = OutputManager()
		self.data = []
		self.headers = []
		self.output.output("init CharacterListView", "status")

	def build(self):
		self.data = self.controller.StringList(self.controller.getRecords("Characters"))
		self.headers = self.controller.getHeaders("Characters")
		self.tableKey = "TABLE_KEY"
		layout = [
			[sg.Table(values=self.data,
			headings=self.headers,
			selected_row_colors='white on red',
			auto_size_columns=True,
			enable_events=True,
			enable_click_events=True,
			key=self.tableKey,
			justification='right' )],
	      		[sg.Submit(), sg.Cancel()]
		]

		window = sg.Window(title="Character List View", layout=[layout])
		window.source = self
		self.window = window
		return window

	def loadData(self):
		self.data = self.controller.StringList(self.controller.getRecords("Characters"))
		self.headers = self.controller.getHeaders("Characters")
		self.window[self.tableKey].update(values = self.data, headings = self.headers)

