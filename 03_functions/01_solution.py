def calculate_percentage(eng, math, science):
    total = eng + math + science
    percentage = total / 3
    return percentage

def show_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Failed"

eng = int(input("English Marks"))
math = int(input("Math Marks"))
sci = int(input("Science Marks"))

per = calculate_percentage(eng, math, sci)
grade = show_grade(per)

print("Percentage is", per)
print("Grade:", grade)