year = int(input("Please input a year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = False
else:
    leap = False

if leap == True:
	print("\n"+ str(year) + " is a Leap Year.\n")
else:
	print("\n"+str(year) + " is not  Leap Year.\n")