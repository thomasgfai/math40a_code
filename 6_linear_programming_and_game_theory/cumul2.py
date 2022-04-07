#!/usr/bin/python
import random as random

# Total number of entries to consider
n=100

# Create a truncated geometric distribution
l=0.95
p=[0]*n
p[0]=(1-l)/(1-l**n)
for i in range(1,n):
    p[i]=p[i-1]*l

# Create cumulative probabilities
c=[0]*n
c[0]=p[0]
for i in range(1,n-1):
    c[i]=c[i-1]+p[i]
c[n-1]=1.0

# Handwritten bisection routine
def geo2():
    r=random.random()
    lo=0
    hi=n-1

    # Check for boundary case
    if(c[lo]>=r): return 0
    
    # Carry out the bisection
    d=hi-lo
    while(d>1):
        e=lo+(d>>1)
        if(c[e]<r): lo=e
        else: hi=e
        d=hi-lo
    return hi

# Print some random numbers
for i in range(20):
    print geo2()
