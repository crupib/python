import os
import pathlib

os.chdir("/Users/williamcrupi/Documents")
print(pathlib.PurePath.joinpath(pathlib.Path.cwd(), "github"))
