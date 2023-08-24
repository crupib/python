from pathlib import Path 
import os
current_file_path = Path('stat_files.py')
file_stat = current_file_path.stat()
print("File Size in Bytes:", file_stat.st_size)
print("When Most Recent Access:", file_stat.st_atime)
print("When Most Recent Modification:", file_stat.st_mtime)
