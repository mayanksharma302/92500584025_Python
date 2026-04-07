import matplotlib.pyplot as plt

courses = ["MCA", "BCA", "MBA", "BBA"]
students = [120, 80, 60, 40]

max_students = students.index(max(students))

explode = [0,0,0,0]
explode[max_students] = 0.2

plt.pie(students, labels=courses, explode=explode, autopct='%1.1f%%')

plt.title("Students in Each Course")

plt.show()
