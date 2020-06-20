"""
Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying
any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number
of characters and display the count of the number of characters at the end of the document.
"""
import urllib.request

url = input("Website: ")
charcount = 0
try:
    fhand = urllib.request.urlopen(url)
except:
    print('Invalid website')
    quit()
finalstring = ""
for line in fhand:
    words = line.decode().strip()
    for char in words:
        charcount += 1
        if charcount <= 3000:
            finalstring += char
    if charcount <= 3000:
        finalstring += '\n'
print(finalstring)
if charcount > 3000:
    print('Character limit exceeded. Showing the first 3000 characters.')
print('Total number of characters: ', charcount)
