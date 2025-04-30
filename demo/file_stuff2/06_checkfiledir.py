from pathlib import Path 
import os
print("file exists",os.path.exists('hello2.txt'))
print("directory exists",Path('target_folder').exists())
