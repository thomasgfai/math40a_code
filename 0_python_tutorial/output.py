# Open a file called "test" to write it and
# associate it with a file handle called f
f=open("test","w")

# Write some text
f.write("Testing testing\n")

# Write some numbers
for a in range(1,4):
	f.write(str(a)+"\n")

# Close file
f.close()
