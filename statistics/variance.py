# Variance is a measure of the mean difference beetween the mean and the values of a set ^ 2
# We do it sqrt because we want to work with abs values
# Standard deviation = sqrt of variance

import numpy as np
import statistics as stats

dataset1 = [1, 6, 42, 2, 8]
dataset2 = [5, 5, 5, 5, 5]

def var(dataset):
	mean = np.mean(dataset)
	totalSum = 0
	for i in range(len(dataset)):
		diff = np.square(dataset[i] - mean)
		totalSum += diff
	return (totalSum / (len(dataset) - 1))


def stdev(dataset):
	return (np.sqrt(var(dataset)))

print('dataset1 variance: ', var(dataset1))
print('(with numpy): ', np.var(dataset1, ddof=1)) # use simple instead of population
print('dataset1 standard deviation: ', stdev(dataset1))
print('(with numpy): ', stats.stdev(dataset1))

print('dataset2 variance: ', var(dataset2))
print('(with numpy): ', np.var(dataset2, ddof=1)) # use simple instead of population
print('dataset2 standard deviation: ', stdev(dataset2))
print('(with numpy): ', stats.stdev(dataset2))



