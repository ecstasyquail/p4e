"""
Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of
the numbers and print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
"""
import re

fname = input('Filename: ')
try:
    fhand = open(fname)
except:
    quit()

lst = list()
for line in fhand:
    x = re.findall('\S+\s\S+:\s([0-9]+)', line)
    if len(x) < 1:
        continue
    print('debug', x)
    lst.append(int(x[0]))

print(sum(lst) // len(lst))
