import os 
folder_name = "TestFolder"
if(not os.path.exists(folder_name)): 
     os.mkdir(folder_name)
    
os.mkdir(f"{folder_name}/Day 2 of 30 days python challenge")
print("Hello")
print(os.getcwd())
# os.chdir("") use for changing directory
# print(os.getcwd()) use to checking the working directory 
