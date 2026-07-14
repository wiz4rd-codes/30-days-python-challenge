companies = [
    ("Google", 120000),
    ("Amazon", 95000),
    ("Netflix", 150000),
    ("Microsoft", 110000),
    ("Adobe", 85000)
]
expect = int(input("Enter your expected salary : "))
oc = list(filter(lambda x : x[1]>= expect,companies))
print("\Companies Meeting Your Expected Salary:")
for i, (company, salary) in enumerate(oc, start=1):
    print(f"{i}. {company} - ₹{salary}")
