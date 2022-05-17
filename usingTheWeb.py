# there are 2 common formats that we can use when exchanging 
# data across the web. there is eXtendable Markup Language(XML) 
# or JavaScript Oject Notation(JSON).

# XML looks like HTML but XML is more stuctured than HTML.
#example

# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#       +1 734 303 4456
#      </phone>
#      <email hide="yes"/>
# </person>

# another example
import xml.etree.ElementTree as et

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''

tree = et.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
print('Phone: ', tree.find('phone').text)

# calling fromstring converts the string representation of the "tree" 
# XML nodes. calling the find function we can search the tree for the node
# and retrives it



# looping through nodes
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
        <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(f'User count {len(lst)}')

for item in lst:
    print('Name: ',item.find('name').text)
    print('Id: ',item.find('id').text)
    print('Attribute: ', item.get('x'))

# using json
# JSON format is inspired by the object and array from Javascript
# the format for JSON in python, the syntax is how python does 
# dictionaries and lists.
# example
# {
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#     },
#     "email" : { 
#         "hide" : "yes"
#     }
# }

# example
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# it would print the users in the tree.

# when application-to-application conctract each other it is called
# an Application Program Interface,API. We can use an API, where one
# program makes a set of services applications and published the APIs. 
 
# when we create a program where we use services provided by other programs
# it is called Service-Oriented Architecture,SOA. 


# google has an API for free where we can access to their database
# geographic information.


# example using JSON. the program is going to ask for a location then its going
# call Google geocoding API, then return all the information in a JSON

import urllib.request,urllib.parse,urllib.error
import json

service = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
  address = input('Enter location: ')
  if len(address < 1): break
  url = service + urllib.parse.urlencode({'sensor': 'false','address': address})

  print('Retrieving',url)
  uh = urllib.request.urlopen(url)
  data = uh.read().decode()
  print('Retrived',len(data),'characters')

  try:
    js = json.load(data)
  except:
    js = None
  
  if not js or 'status' not in js or js['status'] != 'OK':
    print('=== Failure To Retrieve')
    print(data)
  continue


  print(json.dumps(js,indent=4))
  lat = js["results"][0]["geometry"]["location"]["lat"]
  lng = js["results"][0]["geometry"]["location"]["lng"]
  print('lat',lat,'lng',lng)
  location = js['results'][0]['formatted_address']
  print(location)
  
# vendors would send an API key. the key is used as security and usage.
# a common technology that is used to sign requests over the internet is OAuth.
# more info: www.oauth.net


