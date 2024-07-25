"""
1. Write a Python program to count the occurrences of each word in a
given sentence
string = “To change the overall look of your document. To change the look
available in the gallery”

"""
str = input("Enter a string : ")
ch = input("Enter char : ")
count = 0
for i in str:    # i= str[2]
    if i == ch:
        count += 1

print("Char occurrence : ", count)

word = input("Enter a word : ")

# convert this string into list
# split function
str1 = str.split()
# str1 [0] = hello
# str1 [1] = how
# str1 [2] = are
# str1 [3] = you

# str = hello how are you
count = 0
for w in str1:  #  w = str[0]=hello
    if w == word:
        count += 1
print("occurrence of word : ", count)

print("existence of char i : ", 'i' in str)

if ch in str:
    print("char found!!")
else:
    print("char not found!!")