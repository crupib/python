from zipfile import ZipFile
from glob import glob
from pathlib import Path
with ZipFile('text_files.zip', 'w') as file:
     for txt_file in Path().glob('target_folder/*.txt'):
       print(f"*Add file: {txt_file.name} to the zip file")
       file.write(txt_file)
