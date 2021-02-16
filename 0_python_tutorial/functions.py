# Factorial function
def fac(n):
	b = 1
	for c in range(1, n+1):
		b *= c
	return b

# Recursive factorial function
def rfac(n):
	if n < 2:
		return 1
	else:
		return n*rfac(n-1)

# Call the functions
print "6! =", rfac(6)
print "12! =", fac(12)
print "30! =", fac(30)
