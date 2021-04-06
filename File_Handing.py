file = open("Lexcrop.txt", "r")   # to read the Whole File.
print(file.readable())            # Return True Or False depend upon the File is readable or not.
print(file.read())
file.close()
'''
another way of reading the whole the file, using the for Loop.
for i in file.readlines():
    print(i)

reading just one line in the file.
print(file.readlines()[1])

'''