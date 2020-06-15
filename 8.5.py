"""
Exercise 5: Write a program to read through the mail box data and when you find line that starts with “From”, you will
split the line into words using the split function. We are interested in who sent the message, which is the second word
on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line, then you will also count the number of
From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed:

python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
"""
fhand = ""
emails = ""
count = 0
while True:
    #gets user inputed filename
    fname = input("Please enter filename: ")
    #tries to open file
    try:
        fhand = open(fname)
    # reprompts for file name
    except:
        print("Invalid file please try again.")
        continue
    break

# goes through each line in file
for line in fhand:
    #checks for line to start with "From" or skips it
    wordlist = line.split()
    if len(wordlist) == 0:
        continue
    if wordlist[0] != "From":
        continue
    #splits line
    splitline = line.split()
    #grabs email the second element
    emails = splitline[1]
    #counts if we had a line
    count += 1
    #prints out emails
    print(emails)
print("There were %i lines in the file with From as the first word" %count)
