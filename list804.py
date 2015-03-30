fhand = open('romeo.txt')
for line in fhand:
	t = line.split()
	for word in t:
		if word in t == True: continue
		t1 = t.append(word)
print t1
			
	