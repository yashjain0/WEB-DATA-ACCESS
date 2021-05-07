import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
data.decode()
info = json.loads(data)
infog=info['comments']
print(infog)
print('User count:', len(infog))

total=0
for item in infog:
    total=int(item['count'])+total
print('total')
