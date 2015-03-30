fname = raw_input('Enter a file name:\n')
fhand = open(fname)
d = dict()
greatest = None
greatestname = None
for line in fhand:
	if line.startswith('From'):
		words = line.split()
		print words
		if len(words) > 2:
			#print words
			date = words[1]
			if date not in d:
				d[date] = 1
			else:
				d[date] = d[date] + 1
for man in d:
	if d[man] > greatest:
		greatest = d[man]
		greatestname = man
print d
print greatestname, greatest