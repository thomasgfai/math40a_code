
# String of text
a='She sells she she sea shells on the sea shore'

# Split elements into a list
b=a.split(' ')


# Count the words
c={}
for w in b:
	if(w in c):

		# Add 1 to existing counter
		c[w]+=1
	else:
		
		# New counter
		c[w]=1

# Print frequencies
for w,f in c.iteritems():
	print w,f
