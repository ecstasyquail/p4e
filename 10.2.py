"""
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour
from the “From” line by finding the time string and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
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

hour = dict()
# goes through each line of file skips lines without right info,
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    # breaks down the time into 3 sections
    num = list(words[5].split(':'))
    # populates dict with hour and counts
    hour[num[0]] = hour.get(num[0], 0) + 1

# creates a list of tuples with key first
temp = list()
for k, v in hour.items():
    temp.append((k, v))

# sorts list from smallest to biggest
temp.sort()

# uncomment to print name first followed by value
for k, v in temp:
    print(k, v)
