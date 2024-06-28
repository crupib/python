import matplotlib.pyplot as plt
from sound import Sound

sound = Sound('mono')
X, Y = sound.time, sound.data
Y3000 = sound.lowpass(3000)

plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.ylim(-1, 1)
plt.plot(X, Y), plt.plot(X, Y3000)
plt.subplot(122)
plt.xlim(0.2, 0.21), plt.ylim(-1, 1)
plt.plot(X, Y), plt.plot(X, Y3000)
plt.show()
#plt.savefig('lowpass.png', bbox_inches='tight', pad_inches=0)
