import PIL.Image as Img
import matplotlib.pyplot as plt
import numpy as np

im0 = Img.open('mypict.jpg')
im1 = np.asarray(im0)

plt.imshow(im1)
#plt.show()
plt.savefig('mypict_plot.pdf', bbox_inches='tight', pad_inches=0)
