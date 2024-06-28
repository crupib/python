from numpy import array, random, linalg, sqrt
import matplotlib.pyplot as plt

random.seed(2021)
n = 50
mu, sigma, tau = 10, 2, 1

U1, U2 = random.normal(mu, sigma, (2, n))
Error1, Error2 = random.normal(0, tau, (2, n))
V1, V2 = U1 + Error1, U2 + Error2
W1 = (sigma**2 * V1 + tau**2 * mu) / (sigma**2 + tau**2)
W2 = (sigma**2 * V2 + tau**2 * mu) / (sigma**2 + tau**2)

plt.figure(figsize=(7, 7))
plt.xlim(mu-sigma*2, mu+sigma*2), plt.ylim(mu-sigma*2, mu+sigma*2)
plt.scatter(U1, U2, s=50, marker='o')
plt.scatter(V1, V2, s=50, marker='x')
plt.scatter(W1, W2, s=50, marker='s')

UV = UW = 0
for u1, u2, v1, v2, w1, w2 in zip(U1, U2, V1, V2, W1, W2):
    plt.plot([u1, v1], [u2, v2], color='gray')
    plt.plot([u1, w1], [u2, w2], color='gray')
    UV += sqrt((u1 - v1)**2 + (u2 - v2)**2)
    UW += sqrt((u1 - w1)**2 + (u2 - w2)**2)

print(f'U-V: {UV / n}')
print(f'U-W: {UW / n}')
plt.show()
#plt.savefig('estimate.png', bbox_inches='tight', pad_inches=0.05)
