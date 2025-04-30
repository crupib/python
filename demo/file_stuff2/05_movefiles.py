from pathlib import Path
from glob import glob
target_folder = Path("target_folder")
target_folder.mkdir(parents=True,exist_ok=True)
source_folder = Path('.')
txt_files = source_folder.glob('*.txt')
for txt_file in txt_files:
     filename = txt_file.name
     target_path = target_folder.joinpath(filename)
     print(f"** Moving file {filename}")
     print("Target File Exists:", target_path.exists())
     txt_file.rename(target_path)
     print("Target File Exists:", target_path.exists(), '\n')
