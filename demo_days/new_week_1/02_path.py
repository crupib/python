import pathlib

paths = list(pathlib.Path("/etc").iterdir())
paths.sort()
for i in paths:
    print(i)
