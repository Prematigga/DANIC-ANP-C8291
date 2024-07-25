"""
 Write a Python program to reverse words in a string
String = “Deeptech Python Training”

"""
# Deeptech Python Training
str = input("enter a string :")
str1 = str.split()
str2 = " "
for word in str1:
    str2 += word[:: -1] + " "
print(str2)