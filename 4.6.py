"""
4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Award
time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of
time-and-a-half in a function called computepay() and use the function to do the computation. The function should
return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should
use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the
user input unless you want to - you can assume the user types numbers properly.
"""

"""
computepay(hours, rate)
takes hours worked and rate of pay to figure final pay including time and a half after 40 hours
hours = number of hours worked
rate = current rate of pay
returns float
ex: computepay(40, 10.00)
    400.00
"""
def computepay(strhours, strrate):
    hours = float(strhours)
    rate = float(strrate)
    othours = 0
    otrate = 0

    if hours > 40:
        othours = hours - 40
        otrate = rate * 1.5

    pay = (hours - othours) * rate
    otpay = othours * otrate

    return pay + otpay

while True:

    time = input("Please input the number of hours you have worked: ")
    try:
        hours = float(time)
        if hours < 0:
            print("Please use a positive value")
            continue
        while True:
            pay = input("Please input your current rate of pay: ")
            try:
                rate = float(pay)
                if rate < 0:
                    print("Please use a positive value")
                    continue
            except ValueError:
                print("Please input a number for rate of pay")
                continue
            print("You pay for this period will be", computepay(hours, rate))
            break

    except ValueError:
        print("Please input a number for hours worked")
        continue

    break
