#!/usr/bin/python3

import PySimpleGUI as sg
from Controller import *
from CharacterEditor import *
from CharacterListView import *
from OutputManager import *


def init():
	global controller
	global outputManager

	outputManager = OutputManager()
	outputManager.output("init application", "status")

	controller = Controller("database.db")
	controller.connect()

def characterListView():
	clv = CharacterListView(controller).build()
	while True:
		event, values = clv.read()
		if event == sg.WIN_CLOSED or event == 'Exit':
			break
		if event==clv.source.tableKey:
			data_selected = [clv.source.data[row] for row in values[event]]
			characterEditor(data_selected, clv.source.headers)


	clv.close()

def characterEditor(character, headers):
	ce = CharacterEditor(character, headers,controller).build()
	while True:
		event, values = ce.read()

if __name__=="__main__":
	init()
	characterListView()

