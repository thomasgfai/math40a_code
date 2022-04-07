#!/usr/bin/python

m=9

# Loop over the admissible values
for i in range(m+1):

	# Sum the probability contributions
	p=0.0
	for j in range(i,m+1):
		p+=1.0/(j+1)
	
	# Apply the normalizing factor
	p/=m+1

	# Print the result
	print "%d %g" % (i,p)
