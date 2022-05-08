# instead of using files we can use websites to get data. we would 
# use the a module called sockets . sockets is a built in support 
# in python. using sockets we are able to make connections and retrieve
# data from the internet.


from cmath import pi
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# the program would connect to the server and get the data from the server

# getting an image from the internet
import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((HOST,PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover.jpg HTTP/1.0\n\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if(len(data)<1):break
    time.sleep(0.25)
    count += len(data)
    print(len(data),count)
    picture = picture + data
    
mysock.close()

# looks for the header
pos = picture.find(b"\r\n\r\n")
print(f'Header length {pos}')
print(picture[:pos].decode())

picture = picture[pos+4:]
fhand = open('stuff.jpg','wb')
fhand.write(picture)
fhand.close()

# we can make a web page the same like a file. we use the
# urllib to be able to do it

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# example when we want to see the frequency of each word in the file.
import urllib.request,urllib.parse,urllib.error
f = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') 
count = dict()
for line in f:
    line = line.decode().strip()
    for word in line:
        count[word] = count.get(word,0)+1
        
print(count)



import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


# we are able to use HTML to parse regular expressions to search and 
# extract subtrings


# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://www.dr-chuck.com/page2.htm">
# Second Page</a>.
# </p>

# to extract values we would use href="http://.+?" as our expression
# example:
import urllib.request,urllib.parse,urllib.error
import re
import ssl

# ignore SSl certs
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter - ")
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"',html)
for link in links:
    print(link.decode())

# this example we would get all the links that are in that 
# web page and save them in links using the findall()


# we are able to read binary file using the urllib. we use this if we want
# to extract a non-text file like a image or video.

# example
import urllib.request,urllib.parse,urllib
img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg').read()
f = open('cover.jpg','wb')
f.write(img)
f.close()
# we were able to retrive the image from the web page. it created a new file
# to save it to. the program is going to read all the
# data from the network and it would use the memory in our computer. if the
# size of the file is larger than the amount of memory then the program would crash
# or it would run slowly

import urllib.request,urllib.error,urllib.parse
img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg')
f = open('cover.jpg','wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size += len(info)
    f.write(info)
    
print(f'{size} characters copied.')
f.close()



