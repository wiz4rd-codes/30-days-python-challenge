class File : 
    def __init__(self,name,size):
        self.name = name 
        self.size = size 
    def display(self):
        print(f"File name : {self.name}\nFile size : {self.size}")

class Vault : 
    def __init__(self,vault_name,capacity,files):
        self.vault_name = vault_name
        self.capacity = capacity
        self.files = files

    def status(self):
        self.used_space = 0
        for file in self.files:
            self.used_space += file.size
        self.free_space = self.capacity - self.used_space
        print(f"Used space : {self.used_space}\n")
        print(f"Free space : {self.free_space}\n")

    def add_file(self,name_file,file_size):
        print("\nBefore Adding file : ")
        self.status()
        if(file_size>self.free_space):
            print("Insufficient space ")
            return
        obj_file = File(name_file,file_size)
        self.files.append(obj_file)
        print("File added successfully")
        print("After Adding file : ")
        self.status()

    def remove_file(self, file_name):
        delete = 0
        for file in self.files:
            if(file.name == file_name):
                self.files.remove(file)
                delete = 1
                break

        if(delete == 1):
            print(f"File deleted successfully")
        else : 
            print("No such file exists")

    def search_file(self,file_name):
        found = 0
        for file in self.files:
            if(file.name == file_name):
                print(file.name," : ",file.size)
                found = 1 
                break
        if(found ==1 ):
            print("\nFile found !")
        else :
            print("No such file found \n")

    def show_files(self):
        if(len(self.files) == 0):
            print("Vault Empty")
            return
        for file in self.files:
            print(file.name," : ",file.size)

    def largest_file(self):
        if(len(self.files) == 0):
            print("Vault Empty")
            return
        self.largest = max(self.files,key= lambda file : file.size)
        print(f"\nLargest File : \n{self.largest.name} : {self.largest.size}")
num_files = int(input("Enter number of files you want to enter : "))
files = []
for i in range(num_files):
    name = input(f"Enter name of the file {i+1} : ")
    size = int(input(f"Enter size of the file {i+1} : "))
    file = File(name,size)
    files.append(file)

vault_name = input("Enter vault name : ")
capacity = int(input("Enter vault capacity : "))

vault_obj = Vault(vault_name, capacity, files)
while True:
    print("Choose 1 for Status")
    print("Choose 2 for Add File")
    print("Choose 3 for Remove File")
    print("Choose 4 for Search File")
    print("Choose 5 for Show Files")
    print("Choose 6 for Largest File")
    print("Choose 7 for Exit")

    choice = int(input("Enter choice : "))

    if choice == 1:
        vault_obj.status()

    elif choice == 2:
        name = input("Enter file name : ")
        size = int(input("Enter file size : "))
        vault_obj.add_file(name, size)

    elif choice == 3:
        name = input("Enter file name to delete : ")
        vault_obj.remove_file(name)

    elif choice == 4:
        name = input("Enter file name to search : ")
        vault_obj.search_file(name)

    elif choice == 5:
        vault_obj.show_files()

    elif choice == 6:
        vault_obj.largest_file()

    elif choice == 7:
        print("Exiting Vault...")
        break

    else:
        print("Invalid Choice")

    
