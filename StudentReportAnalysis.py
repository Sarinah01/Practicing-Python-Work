# Student Report Management:
# Learning the use of tuples and Lists:
students=[]
subjects = ("Maths", "Java", "Python")

while True:
    print("1] Add the Student\n2] Display the Student\n3] Give the Analysis\n4] Exit the System")
    choice = input("Enter the choice: ")
    
    match choice:
        case "1":
            num = int(input("Enter the number of students you want to enter: "))
            for i in range(num):
                name = input("Name: ")
                roll = int(input("Roll Number: "))
                marks = input(f"Enter marks in {subjects} [Separated by space]: ").split()
                marks = [int(i) for i in marks]
                student = (name, roll, marks)
                students.append(student)
        
        case "2":
            if not students:
                print("No students to display!")
            else:
                for s in students:
                    name, roll, marks = s
                    print(f"\nName: {name}\nRoll No: {roll}")
                    for i, mark in enumerate(marks):
                        print(f"{subjects[i]}: {mark}")
        
        case "3":
            if not students:
                print("No students to calculate!")
            else:
                while True:
                    choice1 = int(input(
                        "1] Calculate topper Subject wise\n"
                        "2] Overall Topper\n"
                        "3] Average Marks\n"
                        "4] Exit Analysis Menu\n"
                    ))

                    # Initialize variables for subject-wise topper
                    cm, jm, pm = -1, -1, -1
                    cname, jname, pname = "", "", ""

                    # Initialize variables for overall topper
                    total_top = -1
                    total_name = ""

                    # For average calculation
                    highest_avg = -1
                    highest_avg_name = ""
                    sum_subjects = [0] * len(subjects)
                    num_students = len(students)

                    match choice1:
                        case 1:  # Subject-wise topper
                            for s in students:
                                name, roll, marks = s
                                maths, java, python = marks

                                cm, cname = (maths, name) if maths > cm else (cm, cname)
                                jm, jname = (java, name) if java > jm else (jm, jname)
                                pm, pname = (python, name) if python > pm else (pm, pname)

                            toppers = [[cm, cname], [jm, jname], [pm, pname]]
                            for i, t in enumerate(toppers):
                                print(f"{subjects[i]} Topper: {t[1]} with {t[0]} marks")

                        case 2:  # Overall topper
                            for s in students:
                                name, roll, marks = s
                                total_marks = sum(marks)
                                total_top, total_name = (total_marks, name) if total_marks > total_top else (total_top, total_name)

                            print(f"Overall Topper: {total_name} with {total_top} total marks")

                        case 3:  # Average calculation
                            for s in students:
                                name, roll, marks = s
                                avg = sum(marks) / len(subjects)
                                if avg > highest_avg:
                                    highest_avg = avg
                                    highest_avg_name = name
                                for i, mark in enumerate(marks):
                                    sum_subjects[i] += mark

                            for i, total in enumerate(sum_subjects):
                                print(f"Average in {subjects[i]}: {total / num_students:.2f}")

                            print(f"Highest Average: {highest_avg_name} with {highest_avg:.2f} marks")

                            for i, sub in enumerate(subjects):
                                top_mark = max(s[2][i] for s in students)
                                print(f"Highest in {sub}: {top_mark}")

                        case 4:
                            print("Exiting Analysis Menu...")
                            break
        
        case "4":
            print("--- Exiting the System ---")
            break
