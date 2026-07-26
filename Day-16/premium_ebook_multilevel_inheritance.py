class Book : 

    def __init__(self,title ,author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")

class EBook(Book):

    def __init__(self,title ,author,format,size):
        Book.__init__(self,title,author)
        self.file_format = format
        self.file_size = size

    def display(self):
        Book.display(self)
        print(f"File Format : {self.file_format}")
        print(f"File Size : {self.file_size}")

class PremiumEBook(EBook):

    def __init__(self,title,author,format,size,subscription_type,download_limit):
        EBook.__init__(self,title ,author,format,size)
        self.subscription_type = subscription_type
        self.download_limit = download_limit 

    def display(self):
        EBook.display(self)
        print(f"Subscription Type : {self.subscription_type}")
        print(f"Download Limit : {self.download_limit}")

num_premium_ebook = int(input("How many Premium EBooks do you want to enter : "))
premium_ebooks = []

for i in range (0,num_premium_ebook):

    title = input("Premium EBook Title : ")
    author = (input("Author : "))
    file_format = (input("File Format : "))
    file_size = int(input("File Size : "))
    subscription_type = (input("Subscription Type : "))
    download_limit = int(input("Download Limit : "))
    print()

    premium_ebook = PremiumEBook(title,author,file_format,file_size,subscription_type,download_limit)
    premium_ebooks.append(premium_ebook)

for i,premium_ebook in enumerate(premium_ebooks, start = 1):
    print(f"Premium EBook Number : {i}")
    premium_ebook.display()
   

