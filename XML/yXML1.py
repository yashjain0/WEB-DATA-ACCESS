import xml.etree.ElementTree as ET

data = '''
<person>
	<name>Yash</name>
	<phone type="intl">
		+91 9637472847
	</phone>
	<email hide="yes"/>
</person>'''

tree= ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
