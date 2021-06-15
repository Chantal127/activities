import random

first = random.randint(0, 10)
second = random.randint(0, 10)
print ("First Number:" , first)
print ("Second Number:", second)
print ("Operation: \nA: Addition \nB: Subraction \nC: Multiplication \nD: Division \n" )
operation = input("\nChoose Operation: ")
print (operation)
if operation == "A" or operation == "a":
    print ("What is sum?")
    ans = int(input())
    print (ans)
    add = (first + second)
    if add == ans:
     print ("Correct")
    else :
     print ("WRONG: The correct answer is: " + str(add))
elif operation == "B" or operation == "b":
    print ("What is difference?")
    ans = int(input())
    print (ans)
    sub = (first - second)
    if sub == ans:
     print ("Correct")
    else :
     print ("WRONG: The correct answer is: " + str(sub))
elif operation == "C" or operation == "c":
    print ("What is product?")
    ans = int(input())
    print (ans)
    mult = (first * second)
    if mult == ans:
     print ("Correct")
    else :
     print ("WRONG: The correct answer is: " + str(mult))
elif operation == "D" or operation == "d":
    print ("What is Quotient?")
    ans = int(input())
    print (ans)
    div = (first // second)
    if div == ans:
     print ("Correct")
    else :
     print ("WRONG: The correct answer is: " + str(div))

