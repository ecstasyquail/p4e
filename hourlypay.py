# write a simple program to get the user to input their hours, pay rate, and calculate their total pay.

while True:
    hoursinp = input("How many hours have you worked? ")
    # checks to make sure user input a number
    try:
        hoursnum = float(hoursinp)
        while True:
            payrateinp = input("What is your current hourly rate?  ")
            # checks to make sure user input a number
            try:
                payratenum = float(payrateinp)
                # calculates total pay and rounds to 2 decimals
                totpay = round((float(hoursnum) * float(payratenum)), 2)
                print("Your total pay will be " + "$" + str(totpay))
                break
            except ValueError:
                print("Please input a number for your pay rate")
                continue
    except ValueError:
        print("Please input the number of hours worked")
        continue
    break
