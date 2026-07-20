import os
def rename_file(folder,ext):
    count = 1
    files = os.listdir(folder)
    for file in files : 
        st = os.path.splitext(file)
        if(st[1] == ext or st[1]== "."+ ext):
            os.rename(f"{folder}/{file}", f"{count}.{ext}")
            print("File renamed successfully")
            count +=1

folder = input("Enter name of the folder containing files top rename : ")
ext = input("Enter extension : ")
rename_file(folder,ext)
