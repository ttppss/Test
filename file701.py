fname = raw_input('Enter the name of the file please:\n')
try:
	fhand = open(fname)
except:
	print "Error, file cannot be opened.\n"
sppos = 0
total = 0
count = 0
average = 0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):
		sppos = line.find(' ')
		line = line[sppos + 1 :]
		line = float(line)
		count += 1
		total += line
average = total / count
print "Average spam confidence: ", average