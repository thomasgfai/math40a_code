import numpy as np
from skimage import io

# Initialize a 400 x 400 matrix to be
# all zeros (corresponding to black)
a=np.zeros((400,400))

# Create a big white square
for j in range(100,300):
    for i in range(100,300):
        a[j,i]=1.0

# Create a small grey line
for j in range(150,250):
    for i in range(20):
        a[j,j+i]=0.5

# Save the image in PNG format
io.imsave("test.png",a)
