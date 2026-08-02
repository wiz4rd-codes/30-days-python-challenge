import os 
from concurrent.futures import ThreadPoolExecutor

folder = input("Enter path of the folder : ")

os.chdir(folder)
files = files = [file for file in os.listdir() if file.endswith(".txt")]

def count_words(file):

    with open(file , "r") as f : 
          content = f.read()

    words = content.split()
    num_words = len(words)

    return file , num_words

with ThreadPoolExecutor() as exe:
        
        result = exe.map(count_words,files)
        
        for file, count in result:
            print(f"Words in {file} : {count}")
        


