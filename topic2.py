# Task 1: Area and Perimeter of a Rectangle
length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

# Task 2: Compare Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("First number is greater.")
elif num1 < num2:
    print("First number is smaller.")
else:
    print("Both numbers are equal.")

# Task 3: Leap Year Checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year.")
else:
    print("Not a leap year.")

# Task 4: Arithmetic and Logical Operators
a = 10
b = 3
print("Addition:", a + b)
print("Power:", a ** b)
print("Logical AND:", a > 0 and b > 0)
print("Logical OR:", a < 0 or b > 0)

# Task 5: String Concatenation
first = "Anjali"
last = "Shukla"
full = first + " " + last
print("Full Name:", full)
