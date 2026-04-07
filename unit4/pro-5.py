import matplotlib.pyplot as plt

companies = []
employees = []

for i in range(5):
    name = input("Enter company name: ")
    companies.append(name)

    emp = int(input("Enter number of employees: "))
    employees.append(emp)

plt.bar(companies, employees)
plt.xlabel("Company Name")
plt.ylabel("Employee Size")
plt.title("Company Employee Size")
plt.show()
