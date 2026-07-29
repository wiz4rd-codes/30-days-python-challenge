import shutil
import os 

ch_dir = input("Enter path of the folder you want to organize : ")
os.chdir(ch_dir)
sub_folder = input("Is your files are in sub folder?\nYes or No\nEnter : ")
if(sub_folder.capitalize() == "Yes"):
    sub = input("Enter subfolder name : ")
    dir_list = os.listdir(sub)
    
    items = ["images","pdfs","videos","python_files","text_files","others"]
    for item in items: 
        if not os.path.exists(os.path.join(sub, item)):
            os.makedirs(os.path.join(sub, item))
    for item in dir_list:
        source = os.path.join(sub,item)
        it = item.split(".")
        if(it[-1]=="png" or it[-1]=="jpeg" or it[-1]=="jpg"):
            shutil.move(source,os.path.join(sub,"images"))
        elif(it[-1]=="pdf"):
            shutil.move(source,os.path.join(sub,"pdfs"))
        elif(it[-1]=="mp4" or it[-1] == "mkv" or it[-1] =="mov"):
            shutil.move(source,os.path.join(sub,"videos"))
        elif(it[-1]=="py"):
            shutil.move(source,os.path.join(sub,"python_files"))
        elif(it[-1]=="txt"):
            shutil.move(source,os.path.join(sub,"text_files"))
        else :
            shutil.move(source,os.path.join(sub,"others"))
else:   
    dir_list = os.listdir()
   
    items = ["images","pdfs","videos","python_files","text_files","others"]
    for item in items:  
        if not os.path.exists(item):
         os.makedirs(item)
    for item in dir_list:
        it = item.split(".")
        if(it[-1]=="png" or it[-1]=="jpeg" or it[-1]=="jpg"):
            shutil.move(item,"images")
        elif(it[-1]=="pdf"):
            shutil.move(item,"pdfs")
        elif(it[-1]=="mp4" or it[-1] == "mkv" or it[-1] =="mov"):
            shutil.move(item,"videos")
        elif(it[-1]=="py"):
            shutil.move(item,"python_files")
        elif(it[-1]=="txt"):
            shutil.move(item,"text_files")
        else :
            shutil.move(item,"others")
print("Folder organized successfully")
