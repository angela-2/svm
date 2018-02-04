import numpy as np
from matplotlib import pyplot as plt

# Define some test data
# x,y,bias but we can ignore bias
x = np.array([
    [-2,4,1],
    [4,1,-1],
    [1,6,-1],
    [2,4,-6],
    [6,2,-1],
])

# associated output labels
y = np.array([-1,-1,1,1,1])

# plot these examples on a 2D graph
for d, sample in enumerate(x):
    # plot the negative samples (the first 2)
    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidth=2)
        # plot the positive samples (the last 3)
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidth=2)

# print a possible hyperplane
plt.plot([-2,6],[6,0.5])
plt.show()
