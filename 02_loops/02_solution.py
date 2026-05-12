movies = ["Avenger", "Batman", "John Wick", "Interstellar"]

total_bill = 0

for movie in movies:

    print("\nMovie:", movie)
    booking = input("Do you want tickets for this movie? ")
    if booking == "yes":
        tickets = int(input("How many tickets?"))

        price = 800 * tickets

        print("Ticket price:", price)

        if tickets >= 5:
            print("Group Discount applied")
            price = price - 500

        total_bill = total_bill + price

    else:
        print("Skipped")

print("\nFinal bill: ", total_bill)

if total_bill > 5000:
    print("Free popcorn included ")

else:
    print("No free popcorn ")