class Student:

    def AddStudent(self):
        self.rollno = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender: ")

    def DisplayStudent(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

s = Student()
s.AddStudent()
s.DisplayStudent()
