"""
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the
values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

fhand = open('words.txt')
worddict = {}
for lines in fhand:
    words = lines.split()
    for word in words:
        if not word in worddict:
            worddict[word] = 1
while True:
    wordsearch = input('Please enter the word you are looking for or "done" when finished: ')
    if wordsearch.lower() == 'done':
        print('See you next time.')
        break
    elif wordsearch in worddict:
        print('Your word is in the text')
        continue
    else:
        print('Sorry your word is not in the text.')
        continue
