import PIL.Image as Img
import glob

f = 'Audacity2'

im = Img.open(f'../{f}.png')
x, y = im.size
im.thumbnail((x*128/y, 128))
im.save(f'thumb_{f}.png')

