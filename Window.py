import PySimpleGUI as sg

layout = [[sg.Text('Create New Object')], 
                 [sg.InputText(key="NameInput")],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window(title="Hello World", layout=[layout], margins=(200, 150))
while True:
	event, values = window.read() 
	window["NameInput"].Update('')
	print (event, values)
	if event == sg.WIN_CLOSED or event == 'Exit':
		break

window.close()
