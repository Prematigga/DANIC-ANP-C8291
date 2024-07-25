files = open("C:\\Users\\Anudip\\Documents\\ritesh.txt", "r")
count = 0
content = files.read()
# Splitting the words: wordList = files.read().split()
for i in content:
    # print(i)
    if ord(i) == 32:
        count += 1
print(count)
files.close()