import os
import shutil
from pathlib import Path 
source_file = "target_folder/hello.txt"
target_file = "hello2.txt"
target_file_path = Path(target_file)
print("* Before copying, file exists:", target_file_path.exists())
shutil.copy(source_file, target_file)
print("* After copying, file exists:", target_file_path.exists())
