def analyze_student_marks():
    total_marks = 0
    passed_students = 0
    failed_students = 0

    try:
        n = int(input("Enter number of students: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    for i in range(n):
        while True:
            try:
                mark = int(input(f"Enter marks for student {i+1} (0-100): "))
                
                if 0 <= mark <= 100:
                    break
                print("Error: Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid integer.")

        total_marks += mark

        if mark >= 40:
            passed_students += 1
        else:
            failed_students += 1

    average_marks = total_marks / n if n > 0 else 0

    print("\n--- Student Marks Analysis ---")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.1f}")
    print(f"Passed Students: {passed_students}")
    print(f"Failed Students: {failed_students}")

if __name__ == "__main__":
 analyze_student_marks()