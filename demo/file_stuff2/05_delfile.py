import os
print(f"* Before deleting file {os.path.isfile('tmp.txt')}")
os.remove('tmp.txt')
print(f"* After deleting file {os.path.exists('tmp.txt')}")
print(f"* Before deleting directory {os.path.isdir('tmp_folder')}")
os.rmdir('tmp_folder')
print(f"* After deleting directory {os.path.exists('tmp_folder')}")
