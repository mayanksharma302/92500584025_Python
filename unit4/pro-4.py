import matplotlib.pyplot as plt

profit = []

for i in range(5):
    p = int(input("Enter profit for year " + str(i+1) + ": "))
    profit.append(p)

years = [1,2,3,4,5]

plt.plot(years, profit, marker='o')
plt.xlabel("Year")
plt.ylabel("Profit")
plt.title("Profit of 5 Years")
plt.show()
