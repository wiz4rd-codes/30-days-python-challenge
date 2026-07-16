class Book : 
    name = ""
    author = ""
    price = int()
book_list = []
a = int(input("How many books do you want to enter : "))
for i in range (0,a):
    book = Book()
    book.name = input(f"Enter name of the book {i+1} : ")
    book.author = input(f"Eter author's name of the book {i+1} : ")
    book.price = int(input(f"Enter price of the book {i+1} : "))
    book_list.append(book)

for i,book in enumerate(book_list, start = 1):
    print(f"Book {i} ")
    print(f"Name : {book.name}\nAuthor : {book.author}\nPrice : {book.price}")
