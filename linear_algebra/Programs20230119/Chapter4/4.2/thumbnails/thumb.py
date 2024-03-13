import PIL.Image as Img

name = 'mypict5'
im = Img.open(f'{name}.png')
im.thumbnail((128, 128))
im.save(f'thumb_{name}.png')
