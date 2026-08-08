import os
folder = input("Enter path of the folder : ")
search = input("Enter file name you want to search : ")
files = os.listdir(folder)
found = []
for file in files :
    if search.lower() in file.lower() : 
        found.append(file)
if found :
    print("Found : ")
    for file in found:
        print(file)
    print(f"Total Files Found : {len(found)}")
else : 
    print("No such file found")        
