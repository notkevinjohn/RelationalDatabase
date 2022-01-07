import PySimpleGUI as sg
from Controller import *
from CharacterEditor import *
from OutputManager import *

class CharacterListView():
	def __init__(self, controller):
		self.controller = controller
		self.output = OutputManager()
		self.data = self.controller.StringList(self.controller.getRecords("Characters"))
		self.headers = self.controller.getHeaders("Characters")
		self.output.output("init CharacterListView", "status")

	def build(self):
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

		sg.theme("Dark")
		window = sg.Window(title="Character List View", layout=[layout])
		window.source = self
		return window

#while True:
#	event, values = window.read()
#	if event==tableKey:
#		record =  (data[values[tableKey][0]])
#		characterEditor = CharacterEditor(record, headers)
#		while True:
#			event2, value2 = characterEditor.read()
#			if event2 == sg.WIN_CLOSED or event2 == 'Exit':
#				break

#	print ("values", values)
#	if event == sg.WIN_CLOSED or event == 'Exit':
#		break

#window.close()

