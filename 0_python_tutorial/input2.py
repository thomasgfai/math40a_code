# Open "in_test2" file for reading
f=open("in_test2","r")

# Create empty list
q=[]

# Read entire file
for s in f:

    # Remove newline character
    #s=s.strip()

    # Split entries and print
    c=s.split(',')
    print c

    # Also store second column
    q.append(c[1])

# Close file
f.close()

# Print list
print
print q
