class Placement:
    def __init__(self, drive_name):
        self.drive_name = drive_name

    def check_students(self):
        num_students = int(input("Enter number of students to check: "))
        
        for i in range(num_students):
            print(f"\nChecking Student {i+1}:")
            name = input("Name: ")
            cgpa = float(input("CGPA: "))
            backlogs = int(input("Current Backlogs: "))

            # Eligibility logic
            if cgpa >= 7.5 and backlogs == 0:
                status = "Eligible for Interview"
            elif cgpa >= 6.0 and backlogs <= 2:
                status = "Eligible for Written Test only"
            else:
                status = "Not Eligible"
            
            print(f"Result for {name}: {status}")

# Execution
tcs_drive = Placement("TCS Ninja")
tcs_drive.check_students()