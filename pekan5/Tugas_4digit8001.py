
# PROGRAM: FRAMED PALINDROMIC CRYSTAL HOURGLASS
# PRACTICUM WEEK 5

print("=== FRAMED PALINDROMIC CRYSTAL HOURGLASS (WEEK 5) ===")

n_8001 = int(input("Enter the hourglass scale size (N): "))

# =========================
# TOP HORIZONTAL BORDER
# =========================
print("#", end="")

for i_8001 in range(4 * n_8001 + 5):
    print("=", end="")

print("#")


# =========================
# PHASE 1: UPPER HOURGLASS
# =========================
for row_8001 in range(n_8001, 0, -1):

    print("| ", end="")

    # Left balancing spaces
    for space_8001 in range(2 * (n_8001 - row_8001)):
        print(" ", end="")

    # Descending numbers
    for number_8001 in range(row_8001, 0, -1):
        print(number_8001, end=" ")

    # Center crystal axis
    print("<*>", end="")

    # Ascending numbers
    for number_8001 in range(1, row_8001 + 1):
        print(" ", end="")
        print(number_8001, end=" ")

    # Right balancing spaces
    for space_8001 in range(2 * (n_8001 - row_8001)):
        print(" ", end="")

    print("|")


# =========================
# PHASE 2: CENTER AXIS
# =========================
print("|", end="")

for space_8001 in range(2 * n_8001 + 1):
    print(" ", end="")

print("<*>", end="")

for space_8001 in range(2 * n_8001 + 1):
    print(" ", end="")

print("|")


# =========================
# PHASE 3: LOWER HOURGLASS
# =========================
for row_8001 in range(1, n_8001 + 1):

    print("| ", end="")

    # Left balancing spaces
    for space_8001 in range(2 * (n_8001 - row_8001)):
        print(" ", end="")

    # Descending numbers
    for number_8001 in range(row_8001, 0, -1):
        print(number_8001, end=" ")

    # Center crystal axis
    print("<*>", end="")

    # Ascending numbers
    for number_8001 in range(1, row_8001 + 1):
        print(" ", end="")
        print(number_8001, end=" ")

    # Right balancing spaces
    for space_8001 in range(2 * (n_8001 - row_8001)):
        print(" ", end="")

    print("|")


# =========================
# BOTTOM HORIZONTAL BORDER
# =========================
print("#", end="")

for i_8001 in range(4 * n_8001 + 5):
    print("=", end="")

print("#")