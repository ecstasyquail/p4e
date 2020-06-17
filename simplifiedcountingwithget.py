numofstudents = {}
names = ["bob", "bab", 'boo', 'dad', 'mad', 'sad', 'boo', 'fad', 'bob']
for x in names:
    numofstudents[x] = numofstudents.get(x, 0) + 1

print(numofstudents)
