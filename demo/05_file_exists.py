import os, pathlib

os.chdir("/Users/williamcrupi/Documents")
print(os.path.exists("github"))
print(pathlib.Path("github").exists())
