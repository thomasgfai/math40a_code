# Import math functions
from math import *

# Open a file called "test2" to write it and
# associate it with a file handle called f
f=open("test2","w")

# Do formatted output
a=4
b=19.0
c="string"
f.write("%d %f %s\n\n" % (a,b,c))

# Change precision
f.write("pi is %4.3f\n" % pi)
f.write("pi is %4.10f\n\n" % pi)

# Padded output
f.write("   x    x^3\n")
for d in range(11):
	f.write("%4d %6d\n" % (d,d*d*d))

# Close file
f.close()
