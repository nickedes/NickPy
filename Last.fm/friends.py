import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# Last.fm API
my_api_key = "829b12779f358d0af117bef698aaa7e2"

url = "http://ws.audioscrobbler.com/2.0/?"

params = urllib.parse.urlencode({'method': 'user.getFriends', 'user': 'nickedes', 'api_key': my_api_key})

site = urllib.request.urlopen(url+params)

print("friends:")
tree= ET.parse(site)
root=tree.getroot()
x=root.find("friends")
users=x.findall("user")
for i in users:
    print(i.find("name").text)