import os, pathlib

print(os.makedirs(os.path.join(os.getcwd(), "./", "new_folder"), exist_ok=True))
print(
    pathlib.Path(
        pathlib.PurePath.joinpath(pathlib.Path.cwd(), "./", "new_folder2")
    ).mkdir(exist_ok=True)
)
