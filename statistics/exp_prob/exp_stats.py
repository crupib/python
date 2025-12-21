mean = 0
std_dev = 1
from scipy.stats import norm
import numpy as np
import math
samples = np.random.normal(mean, std_dev, 10000)
print(samples)
within_1_std = np.sum(np.abs(samples - mean)<std_dev)
within_2_std = np.sum(np.abs(samples - mean)< 2 * std_dev)
within_3_std = np.sum(np.abs(samples - mean)< 3 * std_dev)
print(f'Percent within 1 standard deviation: {within_1_std / 100}%')
print(f'Percent within 2 standard deviation: {within_2_std / 100}%')
print(f'Percent within 1 standard deviation: {within_3_std / 100}%')
mu = 0
sigma = 1
z = 1
pdf_value = ((1 / (sigma * math.sqrt(2*math.pi))) * math.exp(-((z - mu)**2)/(2*sigma**2)))
print(f'PDF calculated: {pdf_value}')
pdf_value = norm.pdf(z, mu, sigma)
print(f'PDF norm function at {z} : {pdf_value}')
z = 1
first_probability = norm.cdf(z)
print(f'First probability area calculated: {first_probability}')
z = 1.5
second_probability = norm.cdf(z)
print(f'Second probability area calculated: {second_probability}')
range_probability = second_probability - first_probability
print(f'Range probability calculated: {range_probability}')
print(f'Probability (area) between ' f'1.0 and 1.5: {range_probability * 100}%')