import os
print("Iterate over a root level path: ")
path = "/home/hari/Desktop/python"
for root, dirs, files in os.walk(path) :
    print(root)
    print(dirs)
    print(files)
print("loop over dir and files")
path = input("Enter the directry: ")
for root,dirs,files in os.walk(path) :
    print(root)
    for dir in dirs :
        print(dir)
    for file in files :
        print(file)
