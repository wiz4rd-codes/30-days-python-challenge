import re

with open("data.txt",'r') as f :
    data = f.read()

emails = re.findall("\S+@\S+\.com",data)
ph_numbers = re.findall("[0-9]{10}",data)

print("\n==================EMAILS==================")
for i,email in enumerate(emails, start = 1):
    print(f"{i}. {email}")
print(f"Total emails : {len(emails)}")

print("\n==================PHONE NUMBERS==================")
for i,ph_number in enumerate(ph_numbers, start = 1):
    print(f"{i}. {ph_number}")
print(f"Total Phone Numbers  : {len(ph_numbers)}")
