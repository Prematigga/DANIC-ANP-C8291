"""
Write a Python Count vowels in a string
input= “Welcome to Python Assignment”
Output: Total vowels are: 7
"""
String=input("Enter a String : ")
count = 0
ary = []
for i in String:
    o= i.lower()
    if o == "a"or o == "e" or o == "i"or o == "o" or o == "u":
        count += 1
        print(i)
print(f"Total Number of Vowels : {count}")