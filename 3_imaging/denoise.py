from skimage import data,io
from scipy import ndimage
import numpy as np

# Load in the test image 
o=io.imread("audrey_noise.png", \
	    as_grey=True, dtype='float64')
print(o[:].max())
print(o[:].min())

a=o*(1/o[:].max())

print(a[:].max())
print(a[:].min())

# Initialize a copy of the image 
(y,x)=a.shape
b=np.copy(a)

for j in range(1,y-1):
    for i in range(1,x-1):

        # Create list of nearby points
        l=[a[j-1,i],a[j,i], \
           a[j+1,i],a[j,i+1],a[j,i-1]]

        # Set output pixel to be median
        # of the list
        b[j,i]=np.median(l)

print(b[:].max())
print(b[:].min())

# Plot the image
io.imsave("denoise.png",b)
