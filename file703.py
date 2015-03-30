fname = raw_input('Enter the file name:\n')
try:
	fhand = open(fname)
except:
	fname = fname.lower()
	if fname.startswith('na na boo boo'):
		print "NA NA BOO BOO TO YOU - You have been punk'd"
	else:
		print "File cannot be opened:", fname