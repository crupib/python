# rotation
from scipy import misc,ndimage
face = misc.face()
rotate_face = ndimage.rotate(face, 35)

import matplotlib.pyplot as plt
plt.imshow(rotate_face)
plt.show()
