fname = raw_input("Enter the name of the file please:\n")
try:
	fhand = open(fname)
except:
	print "Error, cannot open the file.\n"
for line in fhand:
		line = line.upper()
		print line
		