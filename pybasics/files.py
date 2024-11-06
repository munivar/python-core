import os

# Python File Open
# f = open("demofile.txt", "r")
# print(f.read())

# Read Only Parts of the File
# f = open("demofile.txt", "r")
# print(f.read(5))

# Read Lines
# f = open("demofile.txt", "r")
# print(f.readline())

# f = open("demofile.txt", "r")
# for x in f:
#   print(x)

# Close Files
# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

# Write to an Existing File
# f = open("demofile.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

#open and read the file after the overwriting:
# f = open("demofile.txt", "r")
# print(f.read())


# Create a New File
# f = open("myfile.txt", "x") # create a new file
# f = open("myfile.txt", "w")

# Delete a File
# os.remove("myfile.txt")

# Check if File exist
# if os.path.exists("myfile.txt"):
#   os.remove("myfile.txt")
# else:
#   print("The file does not exist")

# Create Folder
# os.mkdir("myfolder")

# Delete Folder
# os.rmdir("myfolder")