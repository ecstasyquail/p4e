"""
Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the
line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples
from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

# gets filename and re-prompts until valid or exits with 'done'
while True:
    fname = input('Enter filename or type "done" to finish: ')
    if fname.lower() == 'done':
        quit()
    try:
        fhand = open(fname)
    except:
        print('Invalid Filename')
        continue
    break

emails = dict()
# goes through each line of file skips lines without right info,
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    # populates dict with email addresses and counts
    emails[words[1]] = emails.get(words[1], 0) + 1

# creates a list of tuples with value first
temp = list()
for k, v in emails.items():
    temp.append((v, k))

# sorts list from biggest to smallest
temp.sort(reverse=True)

# uncomment to print name first followed by value
# for v, k in temp[:1]:
#    print(k, v)

# comment out if printing using the above method
print(temp[0])
