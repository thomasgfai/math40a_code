#!/usr/bin/python
from random import random

# Carry out a random walk
def rwalk(steps):
    a=0
    for i in range(steps):
        if(random()<0.5): a+=1
        else: a-=1
    return a

# Total trials
trials=10000

# Starting position
b=[0]*401

# Bin random walk positions
for i in range(trials):
    b[rwalk(400)+200]+=1

# Print distribution
ift=1/float(trials)
for j in range(101):
    k=-100+2*j
    print k,b[k+200]*ift

# Plot distribution
import matplotlib.pyplot as plt
c=[]
d=[]
for j in range(101):
    k=-100+2*j
    c.append(k)
    d.append(b[k+200]*ift)
plt.plot(c,d)
plt.show()
