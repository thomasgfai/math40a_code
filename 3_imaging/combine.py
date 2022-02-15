import numpy as np
from skimage import io

def normsq(x,y):
    return x*x+y*y

# Empty matrix
a=np.zeros((400,400,3))

# Squared radius circles
r=10000

# Output each channel
for j in range(400):
    for i in range(400):

        # Add red circle
        if(normsq(i-130,j-130)<r):
            a[j,i,0]=1

        # Add green circle
        if(normsq(i-270,j-130)<r):
            a[j,i,1]=1

        # Add blue circle
        if(normsq(i-200,j-240)<r):
            a[j,i,2]=1

# Output image
io.imsave("combine.png",a)
