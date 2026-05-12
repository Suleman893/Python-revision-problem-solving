seats = [1, 2, 3, 4, 5, 6, 7, 8]
booked = []

for seat in seats:

    print("\nSeat", seat)

    answer = input("Do you want to book this seat? (yes/no): ")

    if answer == "yes":

        name = input("Enter passenger name: ")

        age = int(input("Enter passenger age:  "))

        booked.append(seat)

        print("Seat booked for", name)

        if age < 12:
            print("Child passenger")

        elif age >= 60:
            print("Senior citizen discount available")

    else:
        print("Seat skipped")

print("\n------ Booking Summary -----")

for seat in booked:
    print("Seat", seat, "is booked")

print("Total booked seats:", len(booked))

remaining = len(seats) - len(booked)

print("Remaining seats:", remaining)