from matplotlib import pyplot as plt
from numpy.random import normal
from numpy import mean, std
from scipy.stats import norm

# Generate a normal distribution sample with mean 50 and standard deviation 5
sample = normal(loc=50, scale=5, size=1000)

# Plot the histogram
plt.figure(figsize=(5, 4)) 
plt.hist(sample, bins=10, density=True)
plt.show()

# Calculate and print the mean and standard deviation
sample_mean = mean(sample)
sample_std = std(sample)
print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))

dist = norm(sample_mean, sample_std)
dist

values = [value for value in range(30,70)]
probabilitas = [dist.pdf(value) for value in values]
probabilitas

plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilitas)
plt.show()