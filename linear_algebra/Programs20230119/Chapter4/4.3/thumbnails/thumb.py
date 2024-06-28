import PIL.Image as Img

name = 'mat_product2'
im = Img.open(f'{name}.png')
im.thumbnail((128, 128))
im.save(f'thumb_{name}.png')
