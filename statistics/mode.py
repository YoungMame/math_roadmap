# The mode in a data set is the most represented value

import statistics as stats

dataset1 = [0, 2, 2, 3, 5, 6, 6, 6, 10, 12, 12, 13]
print('working with dataset1: ', dataset1)
print('the mode is: ', stats.mode(dataset1))

dataset2 = [0, 2, 2, 3, 5, 6, 6, 6, 10, 12, 12, 12, 13]
print('working with dataset2: ', dataset2)
print('the modes are: ', stats.multimode(dataset2))