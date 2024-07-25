
 17:24
ilename= open("C:\\Users\\Anudip\\Documents\\ritesh.txt", "r")
 word_count=0
 with open("C:\\Users\\0013tu\\Downloads\\Sale.txt",'r') as file:
     line=file.read()
     for char in line:
         if char.isupper():
             word_count+=1
 print(f"The Uppercase characters are:{ word_count}")
 filename= ("C:\\Users\\Anudip\\Documents\\ritesh.txt", "r")
 total_words=0
 with  open("C:\\Users\\Anudip\\Documents\\ritesh.txt", "r") as file:
    for line in file:
words=line.split()
        total_words+=len(words)
print(f"The total no. of words are: {total_words}")
xab-iopi-bem