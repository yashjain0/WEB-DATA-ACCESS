import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')


print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
data.decode()
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print(len(lst))

total=0
for item in lst:
	total=int(item.find('count').text)+total	


print(total)
