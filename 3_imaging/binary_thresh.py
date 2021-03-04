import numpy as np
from skimage import io

# Load in the test image 
a=io.imread("audrey.png",as_grey=True)

# Initialize blank image
(y,x)=a.shape
b=np.zeros((y,x))

# Do binary thresholding
for j in range(y):
    for i in range(x):
        if(a[j,i]<128.0):
            b[j,i]=0.0
        else:
            b[j,i]=1.0

# Plot the image
io.imsave("binary.png",b)
