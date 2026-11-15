# Part A
print("=== PART A ===")

username = input("Enter username")

print("Username:", username)
print("Contains only letter and numbers:", username.isalnum())
print("Starts with a letter:", bool(username) and username[0].isalpha())

if len(username) >= 5 and username.isalnum() and username[0].isapha():
    print("Valid username")
else:
    print("Invalid username")

# Part B
print("=== PART B ===")

nim = input("Enter NIM: ")

if len(nim) == 10 and nim.isdidigit():
    year = nim [:2]
    print("Valid, intake year 20" + year)
else:
    print("Invalid NIM")



