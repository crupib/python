import PIL.Image as Img

name = 'mat_product5'
im = Img.open(f'../{name}.png')
x, y = im.size
im.thumbnail((x*128/y, 128))
im.save(f'thumb_{name}.png')
