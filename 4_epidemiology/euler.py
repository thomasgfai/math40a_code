# Import math functions
from math import *

# Initial variables and constants
x=1
t=0
dt=0.05
gamma=0.5

# Apply Euler step until t>6
while(t<=6):

	# Analytic solution
	xexact=exp(-gamma*t)
	
	# Print the solutions and error
	print t,x,xexact,x-xexact
	
	# Euler step
	x=x+dt*(-gamma*x)

	# Update time
	t+=dt
