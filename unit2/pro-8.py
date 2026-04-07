import csv

def process_student_marks(file_name):
    print(f"{'Roll No':<10} {'Name':<15} {'Total':<10} {'Percentage':<12} {'Grade'}")
    print("-" * 55)

    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            
            for row in reader:
                roll_no, name, m1, m2, m3, m4 = row
                
                marks = [int(m1), int(m2), int(m3), int(m4)]
                total = sum(marks)
                percentage = total / 4
                
                
                if percentage >= 85:
                    grade = 'A+'
                elif percentage >= 70:
                    grade = 'A'
                elif percentage >= 50:
                    grade = 'B'
                else:
                    grade = 'F'
                
                # Display the results
                print(f"{roll_no:<10} {name:<15} {total:<10} {percentage:<12.2f} {grade}")
                
    except FileNotFoundError:
        print("Error: The file was not found. Please ensure 'marks.csv' exists.")

process_student_marks('marks.csv')
