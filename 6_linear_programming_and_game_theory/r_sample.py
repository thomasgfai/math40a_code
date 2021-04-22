#!/usr/bin/python
from random import randint

# Test function returning weighted
# random number
m=9
def play():
    return randint(0,randint(0,m))

# Bins to store 
b=[0 for i in range(m+1)]

# Carry out a large number of trials
# and bin the results
trials=100000
for i in range(trials):
    b[play()]+=1

# Output the estimated probabilities
for i in range(m+1):
    print "%d %g" % (i,float(b[i])/trials)
