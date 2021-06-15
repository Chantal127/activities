def add(first, second):
  first += second
  return first
def subtraction(first, second):
  first -= second
  return first
def mul(first, second):
  first *= second
  return first
def division(first, second):
  first /= second
  return first

switcher = {
    1: add,
    2: subtraction,
    3: mul,
    4: division

}
def switch(operation, num1, num2):
  return switcher.get(operation, default)(num1, num2)
print('''You can perform operation
1. Addition
2. Subtraction
3. Multiplication
4. Division''')

choice = int(input("Select operation from 1,2,3,4 : "))
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print (switch(choice, num1, num2))