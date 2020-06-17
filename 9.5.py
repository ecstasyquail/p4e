"""
Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who
the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

# gets filename from user
fname = input('Enter filename: ')
emails = {}

# sanity check
try:
    fhand = open(fname)
except:
    print("Invalid file name.")
    quit()

# breaks down mail log by line
for line in fhand:
    # strips white space
    line = line.rstrip()
    # creates list of words in each line
    words = line.split()
    # skips lines with no words or that do not start with relevant info
    if len(words) == 0 or words[0] != 'From':
        continue
    #creates a list of emaill address and domain name
    domain = words[1].split('@')
    # creates dictionary with the domain name and counts number of occurences.
    emails[domain[1]] = emails.get(domain[1], 0) + 1

print(emails)
