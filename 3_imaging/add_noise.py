import numpy as np
from skimage import io
from random import random,randint

# Load in the test image 
o=io.imread("audrey.png",as_grey=True)
(y,x)=o.shape
a=o*(1/255.0)

# Introduce noise at 2% of points,
# avoiding the borders for simplicity
for i in range(x*y/50):
    a[randint(1,y-2),randint(1,x-2)]=random()

print(a[:].max())
print(a[:].min())

# Plot the image
io.imsave("audrey_noise.png",a)
