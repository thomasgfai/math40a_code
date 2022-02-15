import numpy as np
from skimage import io

# Size of image
m=384; n=512; a=[0]*(m*n)

# Initial sequence
s=[1,2]
a[0]=1
a[1]=2
a[2]=2
k=3
l=2

# Create the bulk of the sequence
while k<m*n:
    k2=k+a[l]
    if k2>=m*n: k2=m*n
    sym=s[l%len(s)]
    while k<k2:
        a[k]=sym
        k+=1
    l+=1

# Save the image in PNG format
b=np.asarray(a,dtype='float64')
b-=1.0
b.shape=(m,n)
io.imsave("test.png",b)
