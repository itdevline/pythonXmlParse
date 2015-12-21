import xml.etree.ElementTree as parse

root = parse.parse('xmlExample.xml')    # Parse XML file
doc = root.getroot()

"""
print(doc.tag)
print(doc.attrib)
"""
"""
rootT = root.find('channel/title')
rootL = root.find('channel/link')
rootD = root.find('channel/description')

print(rootT.tag, rootT.attrib)
print(rootL.tag, rootL.attrib)
print(rootD.tag, rootD.attrib)

print(rootT.text)
print(rootL.text)
print(rootD.text)
"""

"""
for c in root.iterfind('channel'):
    print(c.findtext('title'))
    print(c.findtext('link'))
    print(c.findtext('description'))
"""
"""
for item in root.iterfind('channel/item/values'):
    print(item.findtext('title'))
    print(item.findtext('link'))
    print(item.findtext('description'))
"""

"""
for it in root.iterfind('channel/item'):
    print(it.tag, it.attrib)
"""

rootCount = doc.find('channel/item/values')
print(rootCount.attrib['count'])