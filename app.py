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


def characterEditor(character, headers):
	ce = CharacterEditor(character, headers,controller).build()
	while True:
		event, values = ce.read()
		if event == sg.WIN_CLOSED or event == 'Exit':
			break
		if event == ce.source.cancelEvent:
			break
		if event == ce.source.saveEvent:
			ce.source.save(values)
			clv.source.loadData()
			break
	ce.close()


def characterListView():
	global clv
	clv = CharacterListView(controller).build()
	while True:
		event, values = clv.read()
		if event == sg.WIN_CLOSED or event == 'Exit':
			break
		if event==clv.source.tableKey:
			data_selected = [clv.source.data[row] for row in values[event]][0]
			characterEditor(data_selected, clv.source.headers)
			clv.source.loadData()

	clv.close()



if __name__=="__main__":
	init()
	characterListView()

