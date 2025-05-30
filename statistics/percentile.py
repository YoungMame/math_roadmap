# The percentile is a value in a set where n % of the set is higher

import numpy as np
import statistics as stats

dataset = [-45, 0, -1, 2, 2, 3, 5, 6, 7, 7, 7.3, 6, 6, 10, 12, 12, 13, 42, 120]
print('working with dataset: ', dataset)
print('the percentile 25 percents is: ', np.floor(np.percentile(dataset, 25)));

# Now let's talk about interquartile range
# Use it to  ignoring any extreme values or outliers

q1 = np.percentile(dataset, 25)   #25 % percentile
q3 = np.percentile(dataset, 75)   #75 % percentile
iqr = q3 - q1                  #25% to 75%

# x < q1 − 1.5 × iqr or x > q3 + 1.5 × iqr then x is an outlier (extreme value)

def isOutlier(x):
	if (x < q1 - 1.5 * iqr or x > q3 + 1.5 * iqr):
		return True
	return False

print('is 1332 an outlier: ', isOutlier(1332))
print('is 2 an outlier: ', isOutlier(2))
print('is -45 an outlier: ', isOutlier(-45))

