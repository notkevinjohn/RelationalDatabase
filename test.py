import PySimpleGUI as sg

def main():
    layout = [[sg.Text("INIT", key="-TEXT-")]]
    window = sg.Window("Main Window", layout, margins=(100,100))
    while True:
        event, values = window.read(timeout=10)
        window["-TEXT-"].update("UPDATE")
        if event == "Exit" or event == sg.WIN_CLOSED:
           break
    window.close()

if __name__ == "__main__":
    main()
