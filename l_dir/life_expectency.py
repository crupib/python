import matplotlib.pyplot as plt

def your_life_expectancy(age):
  if age < 85:
     return 72 - 0.8 * age
  return 22 - 0.2 * age

plt.plot(range(100), [your_life_expectancy(i) for i in range(100)])
plt.xlabel('Age')
plt.ylabel('No. Years Left')
plt.grid()
plt.savefig('age_plot.jpg')
plt.show()
