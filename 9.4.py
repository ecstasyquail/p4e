"""Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has
been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum
and minimum loops) to find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

# gets filename from user
fname = input('Enter filename: ')
emails = {}

#sanity check
try:
    fhand = open(fname)
except:
    print("Invalid file name.")
    quit()

# breaks down mail log by line
for line in fhand:
    #strips white space
    line = line.rstrip()
    # creates list of words in each line
    words = line.split()
    #skips lines with no words or that do not start with relevant info
    if len(words) == 0 or words[0] != 'From':
        continue
    #creates dictionary with the email addresses and counts number of occurences.    
    emails[words[1]] = emails.get(words[1], 0) + 1
    
mostemails = None
biggestcount = 0
#itterates the key and value of dict
for k, v in emails.items():
    #checks to see if first time through loop or if  a keys value is larger
    if mostemails is None or biggestcount < v:
        mostemails = k
        biggestcount = v
print(mostemails, biggestcount)
