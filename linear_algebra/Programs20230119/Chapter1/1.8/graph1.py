from numpy import array, zeros
import PIL.Image as Img
import matplotlib.pyplot as plt

im = Img.open('mypict1.jpg')
A = array(im)
m, n = A.shape
avr = A.sum()/m/n
print((m, n), avr)

L = zeros(256)
for i in range(m):
    for j in range(n):
        L[A[i, j]] += 1
        
plt.figure(figsize=(15,5))
plt.plot(range(256), L)
plt.plot([avr, avr], [0, L.max()])
plt.show()
#plt.savefig('graph1.pdf', bbox_inches='tight', pad_inches=0)
