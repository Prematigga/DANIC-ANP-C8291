# Write a Python program to Count all letters, digits, and special
# symbols from the given string
# Input = “P@#yn26at^&i5ve”
# 1. Write a Python program to Count all letters, digits, and special symbols from the given string
# Input = “P@#yn26at^&i5ve”
# Output: Chars = 8 Digits = 2 Symbol = 3
a=input("Enter a string : ")
chars =0
digits=0
symbol=0

for i in a:
    if ord(i)>31 and ord(i)<48 :
        symbol +=1
    elif ord(i)>47 and ord(i)<58:
        digits +=1
    elif ord(i)>64 and ord(i)<123:
        chars +=1
print(f"the total No. of character is : {chars}")
print(f"the total No. of Digits is : {digits}")
print(f"the total No. of Symbols is : {symbol}")