fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
dic=dict()
for lines in fh:
	if lines.startswith('From '):
		words=lines.split()
    #after splitting splitting the 6th word(5th index) by using ':' as the seperator.
		ws= words[5].split(":")
		dic[ws[0]]=dic.get(ws[0],0)+1

for k,v in sorted(dic.items()):
	print(k,v)
