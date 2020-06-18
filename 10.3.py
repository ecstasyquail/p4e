"""
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program
should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits,
punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with the tables at
https://wikipedia.org/wiki/Letter_frequencies.

    Fun fact: The word “tuple” comes from the names given to sequences of numbers of varying lengths: single, double,
    triple, quadruple, quintuple, sextuple, septuple, etc.↩︎

    Python does not translate the syntax literally. For example, if you try this with a dictionary, it will not work as
    you might expect.↩︎
"""

# gets filename and sanity check
while True:
    fname = input('Please enter a file name or enter "done" to quit: ')
    if fname.lower() == 'done':
        quit()
    try:
        fhand = open(fname)
    except:
        print('Invalid filename')
        continue
    break

letters = dict()

# breaks file into lines
for line in fhand:
    # breaks line into words
    words = line.split()
    # breaks words into char
    for word in words:
        tup = tuple(word)
        # ITERATES through chars and if they are alpha, lowers them, adds them to dict and counts
        for char in tup:
            if char.isalpha():
                char = char.lower()
                letters[char] = letters.get(char, 0) + 1

# creates a list of tuples as value key, sorts them big to small
lst = list()
for k, v in letters.items():
    lst.append((v,k))
lst.sort(reverse=True)

# prints out results as key value
for v, k in lst:
    print(k, v)
