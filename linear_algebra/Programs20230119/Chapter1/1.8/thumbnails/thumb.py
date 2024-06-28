import PIL.Image as Img

name = 'mypict2_2'
im = Img.open(f'../{name}.png')
im.thumbnail((128, 128))
im.save(f'thumb_{name}.png')
