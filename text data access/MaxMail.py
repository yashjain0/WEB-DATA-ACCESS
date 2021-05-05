fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count=dict()
maxemail= None
maxcount= None
for lines in fh:
	if lines.startswith('From '):
		words=lines.split()
		count[words[1]]=count.get(words[1],0)+1
#parsing created dictionary to find the mail having the most length.
for a,b in count.items():
	if maxemail==None:
		maxemail=a
		maxcount=b
	elif maxcount<b:
		maxcount=b
		maxemail=a
print(maxemail)
print(maxcount)
