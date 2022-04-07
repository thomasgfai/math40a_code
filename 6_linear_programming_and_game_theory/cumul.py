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

# Function to calculate a random variable
# following the distribution of the p[k]
def geo1():
    r=random.random()
    k=0
    while(r>c[k]):
        k+=1
    return k

# Print some random numbers
for i in range(20):
    print geo1()
