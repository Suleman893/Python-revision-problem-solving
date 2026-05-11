age = int(input("Enter your age : "))
day = input("Enter the day: ")
is_student = input("Are you a student  ?: ")

# Base ticket price
if age < 13:
    price = 8
elif age < 18:
    price = 10
elif age >= 60:
    price = 9
else:
    price = 15

# Wednesday discount
if day.lower() == "wednesday":
    price -= 2

# Student discount
if is_student.lower() == "yes":
    if age <= 25:
        price -= 1
    else:
        print("Student discount only available under age 25")

# Final validation
if price < 5:
    price = 5
print("Your final ticket price is $", price)