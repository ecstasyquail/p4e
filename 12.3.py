"""
Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying
any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number
of characters and display the count of the number of characters at the end of the document.
"""

import socket
url = input("Website: ")
temp = url.split('/')
try:
    host = temp[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    urlcmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = urlcmd.encode()
    mysock.send(cmd)
except:
    print("Invalid website.")
    quit()

charcount = 0
maxcharcount = 3000
while True:
    data = mysock.recv(1)
    charcount += 1
    if len(data) < 1:
        break
    if charcount <= maxcharcount:
        print(data.decode(),end='')
print('\nShowing first %i characters.' %maxcharcount)
print('Total characters:', charcount)

mysock.close()
