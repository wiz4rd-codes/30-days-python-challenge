total_ticket = 100
records = []
while ((name:= input("Enter Customer Name or Enter \"Exit\" to exit\nEnter : ")).capitalize() != "Exit"):
    num_ticket = int(input("Enter Number of Tickets you want to book : "))
    if(total_ticket<num_ticket):
        print(f"Remaining ticket is less than booked ticket\nRemaining ticket : {total_ticket}\nBooking cancelled")
        continue
    total_ticket=total_ticket-num_ticket
    bill = 499*num_ticket
    gst = (18/100)*bill
    final = gst + bill
    records.append({"name" : name,"tickets" : num_ticket,"bill" : bill,"gst" : gst,"final" : final})
    print("Booking successfull")
highest = 0
total_customer = 0
ticket_sold = 0
if len(records) == 0:
    print("No bookings found.")
    exit()
else : 
    for index,record in enumerate(records):
        if(highest<record["final"]):
            highest = record["final"]
            highest_index = index
        for key,value in record.items():
            print()
            print(f"{key} : {value}")
        total_customer +=1
        ticket_sold = record["tickets"] + ticket_sold
print("EVENT REPORT")
print(f"Total Customers : {total_customer}")
print(f"Total Ticket Sold : {ticket_sold}")
print(f"Revenue : {ticket_sold*499}")
print(f"Remaining ticket : {total_ticket}")
print(f"Highest Paying Customer : \n{records[highest_index]["name"]} : {records[highest_index]["final"]}")




