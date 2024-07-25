# WAP to handle a ZeroDivisionError exception when dividing a number by zero.
a = None
b = None
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a/b
    print(result)
except ZeroDivisionError:
    print("ZeroDivisionError")
