students = {}

while True:
    print("\na) Add  b) Search  c) List  d) Update  e) Delete  f) Exit")
    choice = input("Select: ").lower()

    if choice == 'a':
        roll = input("Roll No: ")
        name = input("Name: ")
        m1, m2, m3, m4 = int(input("M1: ")), int(input("M2: ")), int(input("M3: ")), int(input("M4: "))
        total = m1 + m2 + m3 + m4
        perc = total / 4
        grade = "A" if perc >= 75 else "B" if perc >= 50 else "F"
        students[roll] = {"Name": name, "Total": total, "Perc": perc, "Grade": grade}
        print("Added.")

    elif choice == 'b':
        roll = input("Roll No: ")
        if roll in students:
            print(students[roll])
        else:
            print("Not found.")

    elif choice == 'c':
        print(f"{'Roll':<5} {'Name':<10} {'Total':<8} {'%':<8} {'Grade'}")
        for r, s in students.items():
            print(f"{r:<5} {s['Name']:<10} {s['Total']:<8} {s['Perc']:<8.2f} {s['Grade']}")

    elif choice == 'd':
        roll = input("Roll No: ")
        if roll in students:
            students[roll]['Name'] = input("New Name: ")
            print("Updated.")
        else:
            print("Not found.")

    elif choice == 'e':
        roll = input("Roll No: ")
        if students.pop(roll, None):
            print("Deleted.")
        else:
            print("Not found.")

    elif choice == 'f':
        break
