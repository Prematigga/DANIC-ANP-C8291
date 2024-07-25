"""
Write a Python program to count and display the vowels of a given text
String=”Welcome to python Training
"""
# String=”Welcome to python Training”
String=input("Enter a String : ")
count = 0
ary = []
for i in String:
    o= i.lower()
    if i == "a"or i == "e" or i == "i"or i == "o" or i == "u":
        count += 1
        print(i)
print(f"Total Number of Vowels : {count}")