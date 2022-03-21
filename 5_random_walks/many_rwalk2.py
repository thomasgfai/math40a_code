#!/usr/bin/python
from random import random
from math import *

# Total trials and random walk length
trials=100000; n=16

# Bin width and number
bw=0.05; num=1000
b=[[0]*num for i in range(n)]

for i in range(trials):

    # Carry out a small random walk
    x=0
    for j in range(n):

        # Pearson walk step
        x+=cos(2*pi*random())

        # Bin walk position
        k=int((x/bw+num*0.5))
        if k>=0 and k<num: b[j][k]+=1


# Output the frequency density
ift=1/(bw*float(trials))
for k in range(num):
    
    # Assemble a list of entries on one line 
    s=[str(bw*(0.5+k-0.5*num))]
    for j in range(n):
        s.append(str(b[j][k]*ift))

    # Print the line
    print " ".join(s)
