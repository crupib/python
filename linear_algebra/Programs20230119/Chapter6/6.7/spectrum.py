import matplotlib.pyplot as plt
from sound import Sound

sound1, sound2 = Sound('CEG'), Sound('mono')

plt.figure(figsize=(15, 5))
plt.subplot(121)
plt.plot(*sound1.power_spectrum((-1000, 1000)))
plt.subplot(122)
plt.plot(*sound2.power_spectrum())
plt.show()
#plt.savefig('spectrum.png', bbox_inches='tight', pad_inches=0)
