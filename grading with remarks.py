name = input("Plese input Name:\n")

prelim = int(input("Please input Pre-lim: \n"))
mid = int (input("Please input Mid Term: \n"))
semis = int (input("Please input Semi Finals: \n"))
finals = int (input("Please input Finals: \n"))
average = ((prelim + mid + semis + finals)//4)

if average >= 98 and average <=100:
     print("\n With Highest Honor ")
elif average >= 95 and average <= 97:
     print ("\n With High Honor ")
elif average >= 90 and average <= 94:
     print ("\n With Honor ")
elif average >= 75 and average <= 89:
     print ("\n Passed")
elif average >= 51 and average <= 74:
     print ("\n Failed ")
elif average >100 or average <= 50:
     print("\n Invalid")