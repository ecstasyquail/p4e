# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# keeps asling user for input until proper
while True:
    scoreinp = input("Please enter your score between 0.0 and 1.0 ")
    # test input to make sure it is a number
    try:
        scorenum = float(scoreinp)
    except ValueError:
        print("Please enter a number between 0.0 and 1.0")
        continue
    # tests input to make sure it is in range
    if scorenum >= 0 and scorenum <= 1:
        if scorenum >= 0.9:
            print("A")
        elif scorenum >= 0.8:
            print("B")
        elif scorenum >= 0.7:
            print("C")
        elif scorenum >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("Please enter a number between 0.0 and 1.0")
        continue
    break
