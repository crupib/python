import PIL.Image as Img
import glob

files = glob.glob("../*.png")

for name in files:
    im = Img.open(name)
    x, y = im.size
    im.thumbnail((x*128/y, 128))
    im.save(f'thumb_{name[3:-4]}.png')

