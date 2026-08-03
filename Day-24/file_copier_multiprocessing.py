import os
import shutil
import multiprocessing

def copy_file(source , file, destination_folder):
    shutil.copy(os.path.join(source,file), os.path.join(destination_folder,file))
    print(f"{file} copied")

if __name__ == "__main__":

    source = input("Enter path of the source folder : ")
    destination_folder = input("Enter path of the destination folder : ")
    files = os.listdir(source)

    result = []

    for file in files : 
        ext = file.split(".")

        if(ext[-1]== "txt"):
            p = multiprocessing.Process(target = copy_file, args = (source, file,destination_folder))
            result.append(p)
            p.start()
            

    for r in result : 
        r.join()
    print(f"Total Files Copied : {len(result)}")
