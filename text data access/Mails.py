#file to access emails and their counts from a text file.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count=dict()
maxemail= None
maxcount= None
for lines in fh:
	if lines.startswith('From '):
		words=lines.split()
    #updating dictionary
		count[email]=count.get(words[1],0)+1
for a,b in count:
	if maxmail==None or maxcount<b:
		maxmail=a
		maxcount=b
print(maxmail)
print(maxcount)
