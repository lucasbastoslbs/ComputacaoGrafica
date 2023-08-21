import numpy as np
import matplotlib.pyplot as plt
# Change the Size of Graph using
# Figsize
fig = plt.figure(figsize=(4, 4))

# Generating a 3D sine wave
ax = plt.axes(projection='3d')

# Creating array points using
# numpy
x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = y*np.sin(x)
c = x + y

# To create a scatter graph
ax.scatter(x, y, z, c=c)

# turn off/on axis
plt.axis('off')

# show the graph
#plt.savefig('z.jpg')
plt.show()