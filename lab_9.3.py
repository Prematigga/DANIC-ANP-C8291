# Write a python program that opens
# a file and handles a FileNotFoundError exception if the file odes not exist.
filename = input("Enter your file name: ")
try:
    with open(filename) as ff:
        content = ff.read()
except FileNotFoundError:
    print("File does not exist!!!!!")
else:
    print("File found successfully!!!!")
