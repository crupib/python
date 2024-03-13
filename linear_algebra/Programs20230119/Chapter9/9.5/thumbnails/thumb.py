import PIL.Image as Img
import glob

name = "fig9-11.png"
im = Img.open('../'+name)
im.thumbnail((256, 256))
im.save('thumb_'+name)

