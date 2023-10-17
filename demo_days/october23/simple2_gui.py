import PySimpleGUI as sg
import time

# Define the layout of the GUI
layout = [
    [sg.Text('What is your name?'), sg.InputText(key= 'name')],
    [sg.Text('What is your age?'), sg.InputText(key= 'age')],
    [sg.Button('Submit'), sg.Button('Cancel')],
    [sg.Text('', text_color='red', background_color='yellow', key= 'result')]
]

# Create the GUI window
window = sg.Window('My Simple App', layout)

# Event loop to process user input
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Submit' :
        name = values["name"]
        age = values["age"]
        message = f'Hello, {name}! You are {age} years old.'
        # Send this data to somewhere, need 30 seconds to do.
        time.sleep(30)
        # Display Result
        window['result'].update(message)

# Close the GUI window
window.close()
