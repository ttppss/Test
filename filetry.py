fname = raw_input("Enter the file name:\n")
try:
    fhand = open(fname)
except:
    print("File cannot be opened.")
    exit()
count = 0
for line in fhand:
	count += 1
print"There are" , count , "lines in" , fname