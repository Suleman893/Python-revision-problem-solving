score = int(input("Enter your score: "))
attendance = int(input("Enter attendance percentage: "))
extra_assignment = input("Extra assignment submitted?: ")
discipline_case = input("Any discipline case? (yes/no): ")

# Validation
if score < 0 or score > 100:
    print("Invalid score entered. Please verify again!!")
    exit()

# Base grading
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Attendance rules
if attendance < 75:
    print("Attendance below required limit")
    
    # downgrade grade if the attendance is low
    if grade == "A":
        grade = "B"
    elif grade == "B":
        grade = "C"
    elif grade == "C":
        grade = "D"
    elif grade == "D":
        grade = "F"

# Bonus marks:
if extra_assignment.lower() == "yes":
    if score >= 85 and grade != "A":
        print("Bonus applied due to extra assignment")
        
        if grade == "B":
            grade = "A"
        elif grade == "C":
            grade = "B"
        elif grade == "D":
            grade = "C"

# Discipline penalty:
if discipline_case.lower() == "yes":
    print("Discipline penalty applied")
    
    if grade == "A":
        grade = "B"
    elif grade == "B":
        grade = "C"
    elif grade == "C":
        grade = "D"
    else:
        grade = "F"

# Final remarks
if grade == "A":
    remark = "Excellent"
elif grade == "B":
    remark = "Very Good"
elif grade == "C":
    remark = "Good"
elif grade == "D":
    remark = "Needs Improvement"
else:
    remark = "Failed"

print("Final Grade:", grade)
print("Remark:", remark)