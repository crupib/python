import scipy.ndimage as nd
import numpy as np
import matplotlib.pyplot as plt

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90,90:-90] = 2
im = nd.gaussian_filter(im, 8)

sx = nd.sobel(im, axis = 0, mode = 'constant')
sy = nd.sobel(im, axis = 1, mode = 'constant')
sob = np.hypot(sx, sy)

plt.imshow(sob)
plt.show()
