from OutputManager import *
import PySimpleGUI as sg

class CharacterEditor():
	def __init__ (self, data, headers, controller):
		self.data = data
		self.headers = headers
		self.controller = controller

	def build(self):
		layout = []
		for i in range(0, len(self.data)):
			layout.append([sg.Text(self.headers[i]), sg.Input(self.data[i])])
		layout.append([sg.Button('Cancel'), sg.Button('Save')])
		sg.theme("Dark")
		window = sg.Window(title="Character List View", layout=[layout])
		return window



#if __name__ == "__main__":
#	header = ["id","name","species","description"]
#	data = ["1","Ackbar","Mon Cala","Cool Admiral"]

#	ce = CharacterEditor(data, header)
#	while True:
#		event, values = ce.read()
#		print (event, values)
#		if event == sg.WIN_CLOSED or event == 'Exit':
#			break
#	ce.close()
