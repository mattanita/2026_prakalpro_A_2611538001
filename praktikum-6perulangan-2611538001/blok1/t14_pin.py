
Correct_pin = "1234"
MAX_ATTEMPTS = 3
attempts = 1

pin = input("Enter your PIN: ")

while pin != Correct_pin and attempts < MAX_ATTEMPTS:
    print("Incorrect PIN.")
    attempts += 1
    pin = input("Enter your PIN: ")
    
if pin == Correct_pin:
        print("Access granted.")
else:
         print("account locked")
