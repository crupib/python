from scipy import misc
face = misc.face(gray = True)
lx, ly = face.shape
print(lx)
print(ly)
# Cropping
crop_face = face[lx // 4: -lx // 4, ly // 4: -ly // 4]
import matplotlib.pyplot as plt
plt.imshow(crop_face)
plt.show()

