# Exercise 1: Change the socket program socket1.py to prompt the user for the
# URL so it can read any web page. You can use split(’/’) to break the URL into
# its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition where the user
# enters an improperly formatted or non-existent URL.



from pkgutil import extend_path



def ex1():
    import socket
    try:
        url = input('Enter - ')
    except:
        print('404')
    name = url.split('/')[2]
    print(name)
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect((name,80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
    while True:
        data = mysock.recv(512)
        if len(data) < 1: break
        print(data.decode(),end='')
    
ex1()

# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the
# document.

def ex2():
    import socket
    import sys
    import urllib.parse
    
    
    url = input('Enter - ')
    # try:
    #     valid = validators
    #     if valid != True:
    #         raise ValueError
    # except ValueError:
    #     print('url incorrect')
    #     sys.exit()
    try:
        mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as er:
        print(f'Socket failed to create with error {er}')
    
    # gets the hostname
    host = urllib.parse.urlparse(url)
    
    try:
        host_ip = socket.gethostbyname(host.netloc)
    except socket.gaierror:
        print('Cant get ip')
        
    mysock.connect((host.netloc,80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
    count = 0
    while True:
        data = mysock.recv(512)
        count += len(data)
        if len(data) < 1 or count > 3000: break
        print(data.decode(),end='')
    print(count)
    mysock.close()
    
ex2()

    
    

# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.

def ex3():
    import urllib.request
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    chars = 0
    char_limit = 3000
    for line in fhand:
    # \n is considered a character; this follow commands like wc.
    # Change the following to line.decode().rstrip('\n') if desired
        line = line.decode()
        next_count = chars + len(line)
        if next_count <= char_limit:
            print(line.rstrip('\n'))
        elif chars < char_limit:
            char_remain = char_limit - chars - 1
            print(line[:char_remain])
        chars = next_count
    print(chars)
        
ex3()


# Exercise 4: Change the urllinks.py program to extract and count paragraph (p)
# tags from the retrieved HTML document and display the count of the paragraphs
# as the output of your program. Do not display the paragraph text, only count
# them. Test your program on several small web pages as well as some larger web
# pages.
def ex4():
    from bs4 import BeautifulSoup
    import urllib.request,urllib.parse,urllib.error
    import ssl
    
    # ingore SSL certs
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    
    url = input('Enter url - ')
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    
    count = 0
    tags = soup('p')
    for tag in tags:
        count += 1
    print(count)
    
ex4()    
    
    
# Exercise 5: (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv is
# receiving characters (newlines and all), not lines