import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def use(urls, posn):
	html = urllib.request.urlopen(urls, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	total=1
	for tag in tags:
		if total%posn==0 and total/posn==1:
			tag1=tag.get('href', None)
			print(tag.get('href', None))
		total=total+1
	return tag1



print('done')

html = urllib.request.urlopen(tag1, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

total=1
for tag in tags:
	if total%3==0 and total/3==1:
    #use(tag,3)
		tag2=tag.get('href', None)
		print(tag.get('href', None))
	total=total+1

html = urllib.request.urlopen(tag2, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

total=1
for tag in tags:
	if total%3==0 and total/3==1:
		tag3=tag.get('href', None)
		print(tag.get('href', None))
	total=total+1
