class Book: 
    def __init__(self,title,author,price,pages):
        self.title = title 
        self.author = author 
        self.price = price 
        self.pages = pages 

    def __str__(self): 
        return(f"Title : {self.title}\n"
            f"Author : {self.author}\n"
            f"Price : {self.price}\n"
            f"Pages : {self.pages}") 
    
    def __len__(self):
        return self.pages 
    
    def __gt__(self,other):
        return self.price >other.price
        
    def __eq__(self,other):
        return self.author == other.author and self.title == other.title
    
        
    def compare_pages(self,other):
       return self.pages > other.pages
        
num_book = int(input("How many books you want to enter : "))
books = []

for i in range(0,num_book):
    title = input(f"Title : ")   
    author = input(f"Author : ")   
    price = int(input(f"Price : "))
    pages = int(input(f"Pages : "))
    print()
    book = Book(title,author,price,pages)
    books.append(book)

for i,book in enumerate(books ,start = 1 ):
    print(f"Book Number : {i}")
    print(book)

compare = input("Do you want to compare two books \nEnter : ")
if(compare.capitalize()=="Yes"):
    b1 = int(input("Enter number of first book  : "))
    b2 = int(input("Enter number of second book  : "))
    print(f"{books[b1-1].title} is more expensive") if (books[b1-1]> books[b2-1]) else print(f"{books[b2-1].title} is more expensive") 
    print("Book 1 and Book 2 is same") if (books[b1-1]==books[b2-1]) else  print("Book 1 and Book 2 is not same")
    print(f"{books[b1-1].title} have more pages ") if (books[b1-1].compare_pages(books[b2-1])) else  print(f"{books[b2-1].title} have more pages ")
