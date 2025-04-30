from glob import glob
from pathlib import Path
for py_file in Path().glob('target_folder/*.txt'):
   print('Name with extension:', py_file.name)
   print('Name only:', py_file.stem)
