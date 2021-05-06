
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter Count: '))
posn = int(input('Enter Position: '))
def calcium(url, posne):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	# Retrieve all of the anchor tags
	#1
	total=1
	for tag in tags:
		if total%posne==0 and total/posne==1:
			tag1=tag.get('href', None)
			print(tag.get('href', None))
		total=total+1
	return tag1
#trying to retrive specific url and then the url in the nested urls
tag1=calcium(url, posn)
tag2=calcium(tag1, posn)
tag3=calcium(tag2, posn)
tag4=calcium(tag3, posn)
tag5=calcium(tag4, posn)
tag6=calcium(tag5, posn)
tag7=calcium(tag6, posn)

