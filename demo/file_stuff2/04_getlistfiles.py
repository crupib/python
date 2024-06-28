from pathlib import Path
from glob import glob
txt_files = list(Path('.').glob("*.txt"))
print("Txt files:", txt_files)
files = list(glob('*.txt'))
print("Files that end with txt: ", files)
