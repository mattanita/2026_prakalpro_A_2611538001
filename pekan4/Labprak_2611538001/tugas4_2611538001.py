print("=== ALPRO ADVENTURE PARK TICKET SYSTEM ===")

name_8001 = input("Enter Visitor name : ")
age_8001 = int(input("Enter your age : "))
sim_8001 = input("Do you have a SIM C? (y/t) :") .strip().lower()
ticket_8001 = int(input("Enter number of tickets : "))
if ticket_8001 <= 0:
    print("Wearing: Invalid ticket quantity!")

print("\nRide Package Option (1-5) : ")
print("1. Safari Rimba (Rp 50,000)")
print("2. white water Rafting (Rp 75,000)")
print("3. Extreme ATV (Rp 120,000)")
print("4. Lightning Roller Coaster (Rp 100,000)")
print("5. All-Access VIP (Rp 220,000)")

package_8001 = int(input("Enter package number (1-5):"))

match package_8001:
    case 1:
        ride_8001 = "safiri Rimba"
        price_8001 = 50000
    case 2:
        ride_8001 = "White water Rafting"
        price_8001 = 75000
    case 3:
        ride_8001 = "Extreme ATV"
        price_8001 = 120000
    case 4:
        ride_8001 = "lightning Roller coaster"
        price_8001 = 100000
    case 5:
        ride_8001 = "All-Access VIP"
        price_8001 = 220000
    case 6:
        print("Invalid ride package! ")
        exit( )

print("/n--- RIDE ELIGBILITY ---")

if package_8001 == 3 and age_8001 >= 17 and sim_8001 == 'y':
    print("You are an adult and allowed to ride the ATV by yourself.")
elif package_8001 == 3 and age_8001 >= 17 and sim_8001 != 'y':
    print("You are an adult but cannot ride the AVT. An instructor is required. ")
elif package_8001 == 3 and age_8001 < 17 and sim_8001== 'y':
    print("Invalid identificatoin: You are not old enough to have a SIM C.")
elif package_8001 == 3:
    print("You are underage and cannot ride the ATV.")
elif package_8001 != 3 and age_8001 >= 10:
    print("You are eligible to enter this ride.")
else:
    print("You are notb old enough to enter this ride.")

subtotal_8001 = price_8001 * ticket_8001
total_discount_percent_8001 = 0
is_member_8001 = input("Are you member?  (y/t): ").strip().lower()
promo_valid_8001 = input("Is the promo code valid? (y/t):")

if subtotal_8001 >= 200000:
    total_discount_percent_8001 += 10
if is_member_8001 in [ 'y', 'ya']:
    total_discount_percent_8001 += 5
if promo_valid_8001 in ['y' 'ya']:
    total_discount_percent_8001 += 15
if ticket_8001 >= 5:
    total_discount_percent_8001 += 5

subtotal_8001 = price_8001 * ticket_8001
total_discount_percent_8001 = 0

if subtotal_8001 >= 200000:
    total_discount_percent_8001 += 10

if is_member_8001 in ['y', 'ya']:
    total_discount_percent_8001 += 5

if promo_valid_8001 in ['y', 'ya']:
    total_discount_percent_8001 += 15

if ticket_8001 >= 5:
    total_discount_percent_8001 += 5

nominal_discount_8001 = subtotal_8001 * (total_discount_percent_8001 / 100)
total_payment_8001 = subtotal_8001 - nominal_discount_8001

if total_payment_8001 > 300000:
    service_note_8001 = "Congratulation! yaou are entited to a Free Souvenir."
else:
    service_note_8001 = "Thank you for visitinng."

    print("\n--- PEYMENT DETAILS ---")
    print(f"Visitor Name    : {name_8001}")
    print(f"Ride Package    : {ride_8001}")
    print(f"Ticket Price    : Rp {price_8001:,.0f}")
    print(f"Number of Ticket    : {ticket_8001}")
    print(f"Subtotal    : Rp {subtotal_8001:,.0f}")
    print(f"Total Discount  : {total_discount_percent_8001}% (Rp {nominal_discount_8001:,.0f})")
    print(f"Total Payment   : Rp {total_payment_8001:,.0f}")
    print(f"Service Note    :{service_note_8001}")
    print("Program Completed")