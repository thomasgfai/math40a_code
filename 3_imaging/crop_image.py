import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# Load in the test image 
a=io.imread("mythirlmere.png",as_grey=True)

# Check size
(y,x)=a.shape
print x,"by",y,"pixels"

# Plot a small part of the image, and add the
# interpolation='nearest' option to show
# individual pixels
plt.imshow(a[100:200,100:200],cmap=plt.cm.gray, \
        interpolation='nearest')
plt.show()
