# """
# Write a Python program to remove duplicate characters of a given
# string
# Input = “String and String Function”
# Output: String and Function
str = input("enter a string: ")
str1 =""
for ch in str:
    if ch not in str1:
      str1 += ch


print(str1)
# Remove all the duplicate words from a string
word = ""
wor = str.split()
for chra in wor:
    if chra not in word:
        word += chra+ " "
print(word)