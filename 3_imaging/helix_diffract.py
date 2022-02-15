import numpy as np
from skimage import io
from math import *

m=160
n=160
b=np.zeros((m,n))
d=5.0

R=2.0
a=0.5
P=1.5
x1=-3.5
x2=3.5

for i in range(80):
    print i
    x=x1+(x2-x1)*(i+0.5)/50.
    for j in range(80):
        y=R*sin(2*pi*x/P)-0.5*a+a*(j+0.5)/50.
        for k in range(m):
            kx=-d+2*d/m*(0.5+k)
            for l in range(n):
                ky=-d+2*d/n*(0.5+l)
                b[k,l]+=sin(kx*x)*sin(ky*y)

print b.min(), b.max()
b-=b.min()
b/=b.max()

for k in range(m):
    for l in range(n):
        b[k,l]*=b[k,l]
io.imsave("test.png",b)
