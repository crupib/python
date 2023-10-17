import PySimpleGUI as sg
import time
import threading
from sqlalchemy import create_engine, text, inspect

# Create Database Helper
## SQLITE ENGINE
def sqlite_engine() : return create_engine('sqlite:///db.db')
## SQLITE COMMIT
def sqlite_connection(statement) :
    with sqlite_engine().connect() as c :
        r = c.execute(text(statement))
        c.commit()
    return r
## CREATE TABLE IF NOT EXISTS
def create_if_not_exists() :
    create_statement = """CREATE TABLE IF NOT EXISTS tmp
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name VARCHAR(30), age INTEGER, flag INTEGER);"""
    sqlite_connection(create_statement)
## INSERT INPUT VALUE
def insert_into(name, age) :
    insert_statement = """INSERT INTO tmp (name, age, flag)
                        VALUES ('{name}', '{age}', 0)"""
    sqlite_connection(insert_statement.format(name = name, age = age))
## SELECT THE LASTEST DATA
def select_latest_id() :
    select_max_id = """SELECT id, name, age from tmp 
                    WHERE id = (SELECT MAX(id) FROM tmp) AND flag = 0"""
    r = sqlite_connection(select_max_id)
    return r.fetchall()
## UPDATE FLAG TO 1 WHEN FINISHED
def update_flag(id) :
    update_finished = """UPDATE tmp SET flag = 1 WHERE id = {id}"""
    sqlite_connection(update_finished.format(id= id))

class SimpleWorker : 
    def __init__(self, window : sg.Window) :
        # INIT Worker's variable
        self.run = False
        self.window = window
        
    def start_thread(self) :
        # Only Do something if not running
        if not self.run :
            # Create Thread from job_processing function
            self.job_threading = threading.Thread(target=self.job_processing)
            self.job_threading.start()
    
    def stop_thread(self) :
        # Tell Worker to stop
        self.run = False

    def job_processing(self) :
        # Set to run
        self.run = True
        while self.run :
            # If table not exist >> Pass
            if not inspect(sqlite_engine()).has_table('tmp') : continue
            # Get data from Local Database
            result = select_latest_id()
            # Only Run when there are some data inside
            if len(result) > 0 :
                # INIT VALUES
                id, name, age = result[0]
                message = f'Hello, {name}! You are {age} years old.'
                # Send this data to somewhere, need 30 seconds to do.
                time.sleep(30)
                # Display Result
                self.window['result'].update(message)
                # Set Flag = 1, for finished job
                update_flag(id = id)
            # Delay ## Optional
            time.sleep(1)

# Define the layout of the GUI
layout = [
    [sg.Text('What is your name?'), sg.InputText(key= 'name')],
    [sg.Text('What is your age?'), sg.InputText(key= 'age')],
    [sg.Button('Submit'), sg.Button('Cancel')],
    [sg.Text('', text_color='red', background_color='yellow', key= 'result')]
]

# Create the GUI window
window = sg.Window('My Simple App', layout)
# Create and Start Worker
worker = SimpleWorker(window= window)
worker.start_thread()
# Event loop to process user input
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        worker.stop_thread()
        break
    elif event == 'Submit' :
        # Only Create Table if not exists 
        create_if_not_exists()
        # And Insert Data into Local DB
        insert_into(name= values['name'], age= values['age'])

# Close the GUI window
window.close()
