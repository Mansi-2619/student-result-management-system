#Enter details and marks of the student
def add_student(students):
    name = input("Enter student's name: ")
    marks = []
    for i in range(1,6):
        mark = float(input(f"Enter marks for subject{i}: "))
        marks.append(mark)
    total = sum(marks)
    percentage = total / len(marks)
    grade = calculate_grade(percentage)
    #dict to store student data
    student = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }
    students.append(student)

    with open("results.txt", "a") as file:
        file.write(f"{name},{marks},{total},{percentage:.2f},{grade}\n")

    print("Student result added successfully!\n")


#Function to calculate grade
def calculate_grade(percentage):
    if percentage>=90:
        return "A"
    elif percentage>=75:
        return "B"
    elif percentage>=60:
        return "C"
    elif percentage>=45:
        return "D"
    else:
        return "Fail"
        
        
def view_students(students):
    if students:
        for student in students:
            print("----------------------------")
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
            print("Total:", student["Total"])
            print("Percentage:", student["Percentage"])
            print("Grade:", student["Grade"])
            print("----------------------------\n")
    else:
        print("No record found.")
        return


def main():
    students = []
    while True:
        print("🎓 Student Result Management System")
        print("1. Add Student Result")
        print("2. View All Results")
        print("3. Exit")
        
        choice = int(input("Enter your choice(1-3):"))
        if choice == 1:
            add_student(students)
        elif choice == 2:
            view_students(students)
        elif choice == 3:
            print("Existing program. GoodBye!")
            break
        else:
            print("Invalid choice. Try again.\n")
main()