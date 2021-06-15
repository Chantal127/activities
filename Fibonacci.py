n1, n2 = 0, 1
count = 0
terms = int(input("How many terms? "))

if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence: ",terms,":")
   print(n1)
else:
   print("Fibonacci sequence: ")
   while count < terms:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1