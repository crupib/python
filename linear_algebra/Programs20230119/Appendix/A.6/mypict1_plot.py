import PIL.Image as Img
import matplotlib.pyplot as plt
import numpy as np

im0 = Img.open('mypict1.jpg')
im1 = np.asarray(im0)

plt.imshow(im1, cmap='gray')
#plt.show()
plt.savefig('mypict1_plot.pdf', bbox_inches='tight', pad_inches=0)
