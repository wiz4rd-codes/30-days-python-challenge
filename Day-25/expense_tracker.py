def expense():
    num_expense = int(input("Enter Number of expenses : "))
    if(num_expense == 0):
        print("No expenses ")
        return
    t_expenses = 0
    expenses = []
    for i in range(num_expense):
        expense_name = input("Enter name of the expense : ")
        expense_amount = int(input("Enter expense : "))
        expenses.append((expense_name,expense_amount))
        t_expenses += expense_amount
    for i,expense in enumerate(expenses, start =1 ):
        print(f"Expense {i} : ")
        print(f"{expense[0]} : {expense[1]}")
    print(f"\nTotal Expense : {t_expenses}")
    highest = max(expenses, key=lambda x: x[1])

    print(f"Average Expense : {t_expenses/num_expense}")
    print(f"Highest Expense : \n{highest[0]} :{highest[1]} ")

if __name__ == "__main__":
    expense()
