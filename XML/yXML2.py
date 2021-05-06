import xml.etree.ElementTree as ET

input = '''
<stuff>
	<users>
	<user x="2">
		<id>001</id>
		<name>Chuck</name>
	</user>
	<user x="7">
		<id>009</id>
		<name>brent</name>
	</user>
	</users>
</stuff>'''
#changes into a retrievale and parsable format
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
	print('Name', item.find('name').text)
	print('Id',item.find('id').text)
	print('attr',item.get("x"))
