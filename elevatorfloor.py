# What floor are you on in the United States vs the rest of the world?

# gets user input
floornum = input("What floor number are you on? ")

# FINDS OUT WHERE USER IS AT
while True:
    country = input("Are you in the United States? Y/N ")
    if country == 'Y' or country == 'N':
        break
    else:
        print("Please enter 'Y' for yes or 'N' for no")

if country == 'Y':
    if int(floornum) > 1:
        print("You are on floor", floornum)

    else:
        print("You are on the ground floor")
else:
    if int(floornum) == 0:
        print("You are on the ground floor or floor 1 in the USA")
    else:
        usafloornum = int(floornum) + 1
        print("You are on floor number " + str(usafloornum) + " in the USA.")
