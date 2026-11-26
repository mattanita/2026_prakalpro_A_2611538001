number_of_rows = 4
seats_per_row = 5

# Create the cinema seat map
cinema = []

for i in range(number_of_rows):
    cinema.append(["."] * seats_per_row)

seats_taken = 0

while True:
    # Display the seat map
    for row in cinema:
        print(" ".join(row))

    row_number = int(input("Enter row number (0 to stop): "))

    if row_number == 0:
        break

    seat_number = int(input("Enter seat number: "))

    # Check whether the seat is valid
    if row_number < 1 or row_number > number_of_rows or seat_number < 1 or seat_number > seats_per_row:
        print("Invalid seat.")
    
    elif cinema[row_number - 1][seat_number - 1] == "X":
        print("Seat already taken.")

    else:
        cinema[row_number - 1][seat_number - 1] = "X"
        seats_taken += 1
        print("Seat booked.")

print("Seats taken:", seats_taken)