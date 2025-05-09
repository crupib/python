import os
import pathlib
import platform
from mysr import voice_to_text
def open_file(filename):
    if platform.system() == "Windows":
        os.system(f"explorer {directory}\\files\\{filename}") 
    elif platform.system() == "Darwin":
        os.system(f"open {directory}/files/{filename}") 
    else:
        os.system(f"xdg-open {directory}/files/{filename}") 
directory = pathlib.Path.cwd()
while True:   
    print('Python is listening...')
    inp = voice_to_text().lower()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye!')
        break
    elif "open pdf" in inp: 
        inp = inp.replace('open pdf ','')
        myfile = f'{inp}.pdf'
        open_file(myfile)
        continue
    elif "open word" in inp: 
        inp = inp.replace('open word ','')
        myfile = f'{inp}.docx'
        open_file(myfile)
        continue
    elif "open excel" in inp: 
        inp = inp.replace('open excel ','')
        myfile = f'{inp}.xlsx'
        open_file(myfile)
        continue
    elif "open powerpoint" in inp: 
        inp = inp.replace('open powerpoint ','')
        myfile = f'{inp}.pptx'
        open_file(myfile)
        continue
    elif "open audio" in inp: 
        inp = inp.replace('open audio ','')
        myfile = f'{inp}.mp3'
        open_file(myfile)
        continue
    elif "open video recording" in inp: 
        inp = inp.replace('open video recording ','')
        myfile = f'{inp}.mp4'
        open_file(myfile)
        continue
