# Open "in_test" file for reading
f=open("in_test","r")

# Read entire file
s=f.read()
print s

# Close file
f.close()

# Open file again
f=open("in_test","r")

# Read in line-by-line and print
for d in range(4):
	s=f.readline()
	s=s.rstrip()
	print "Animal",d,":",s

# Close file
f.close()
