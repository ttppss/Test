fname = raw_input('Enter a file name:\n')
try:
    fhand = open(fname)
except:
    print 'Error, file cannot be opened.'
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            
print counts