from pathlib import Path 
import os
print("directory exists using os",os.path.isdir('target_folder'))
print("directory exists using path", Path('target_folder').is_dir())
print("file exists using os", os.path.isfile('hello2.txt'))
print("file exists using path", Path('hello2.txt').is_file())
