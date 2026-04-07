import matplotlib.pyplot as plt

ages = [12,15,18,20,22,25,28,30,32,35,
        40,45,50,55,60,17,19,23,27,29,
        31,33,36,38,41,43,46,48,52,58,
        14,16,21,24,26,34,37,39,42,44,
        47,49,53,56,59,61,65,70,75,80]

bins = [0,10,20,30,40,50,60,120]

plt.hist(ages, bins=bins)

plt.xlabel("Age Group")
plt.ylabel("Number of Students")
plt.title("Age Distribution of Students")

plt.show()
