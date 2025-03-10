from scipy import misc
f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()
face = misc.face(gray = False)
print (face.mean(), face.max(), face.min())
