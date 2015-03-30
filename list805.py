fname = raw_input('Enter a file name:')
fhand = open(fname)
count = 0
for line in fhand:
	if line.startswith('From'):
		count += 1
		t = line.split()
		print t[1]
print 'Threr were', count, 'lines in the file with From as the first word'