from pypdf import PdfWriter 
pdfs = []
merger = PdfWriter()

print("Welcome to PDF Merger ")
num_pdf = int(input("How many pdfs you want to merge : "))

for i in range(0,num_pdf):
    pdf = input("Enter name of the pdf with \".pdf\" extension : ")
    pdfs.append(pdf)
for pdf in pdfs:
    merger.append(pdf)
    
merger.write("Merged.pdf")
merger.close()

print("Merged files successfully !! ")

