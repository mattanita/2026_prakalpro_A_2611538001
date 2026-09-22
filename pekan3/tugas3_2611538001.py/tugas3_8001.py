# WEEK 3ASSIGMENT
# Topic:Python Operators
# Store Transation Simulation and Access Vlidation System 

# Customer and Transation Data

customer_name_8001 = input("Enter Customer Name: ")
customer_status_8001 = input("Enter Customer Status (member/non-member): ")
total_purchase_8001 = float(input("Enter Total Purchase: "))
number_of_items_8001 = int(input("Enter Number of Items: "))
promo_code_8001 = input("Enter Promo Code:")

# Membership Operators

available_promos_8001 = [ "HEMAT10", "HEMAT20", "GRATISONGKIR"]

Promo_available_8001 = promo_code_8001 in available_promos_8001
Promo_not_available_8001 = promo_code_8001 not in available_promos_8001

# Comparison Operators

minimum_purchase_8001 = total_purchase_8001>= 200000
minimum_items_8001 = number_of_items_8001 >=3
is_member_8001 = customer_status_8001 == "member"

# Logocal Operators

gets_discounT_8001 = is_member_8001 and minimum_purchase_8001
gets_promo_8001 = minimum_purchase_8001 and minimum_items_8001
promo_access_8001 = promo_available_8001 or is_member_8001
not_member_8001 = not is_member_8001

# Arithmetic Operators

discount_8001 = 0

if gets_discount_8001:
    discount_8001 = total_purchase_8001 * 10 / 100

    total_payment_8001 = total_purchase_8001 - discount_8001
    average_item_price_8001 = total_payment_8001 / number_of_items_8001
    remainder_8001 = total_purchase_8001 % number_of_items_8001

# Assignment Operator

points_8001 = 0

if gets_promo_8001:
    pionts_8001 += 10

# Identily Operators

code_a_8001 = "STORE"
code_b_8001 = code_a_8001

same_identily_8001 = code_a_8001 is code_b_8001
different_identily_8001 = code_a_8001 is not None

# Bitwise Operators

member_bit_8001 = 0b0001
purchase_bit_8001 = 0b0010
items_bit_8001 = 0b0100
promo_bit_8001 = 0b1000

status_code_8001 = 0

if is_member_8001:
    status_code_8001 |= member_bit_8001

if minimum_purchase_8001:
    status_code_8001 |= purchase_bit_8001

if minimum_items_8001:
    status_code_8001 |= items_bit_8001

if promo_available_8001:
    status_code_8001 |= promo_bit_8001

# Bitwise AND, OR, and XOR

check_member_8001 = status_code_8001 & member_bit_8001
combined_status_8001 = member_bit_8001 | promo_bit_8001

reference_code_8001 = 0b1011
difference_code_8001 = staus_code_8001 ^ reference_code_8001

# Customer Access Rights

member_access_8001 = check_member_8001 == check_member_8001 != 0
free_shipping_access_8001 = promo_code_8001 == "GRATISONGKIR"

# Output

print("\n== STORE TRANSATION SYSTEM ===")

print("\n=== CUSTOMER DATA ===")
print("Customer Status:", customer_status_8001)
print("Customer Status:", customer_code_8001)
print("Total purchase:", "Rp", total_purchase_8001)
print("Number of items:", number_of_items_8001)
print("Promo_code:", promo_code_8001)

print("\n=== VALIDATION RESULTS ===")
print("purchase >= Rp200000:", minimum_purchase_8001)
print("Number_of_Items >=3:", minimum_items_8001)
print("Member Status:", is_Member_8001)
print("Promo Code Available:", promo_available_8001)
print("Gets Discount:", gets_discount_80001)
print("Gets Promo:", gets_promo_8001)

print("\n=== CALCULATION RESULTS ===")
print("Discount: Rp", discount_8001)
print("Total Payment: Rp", total_payment_8001)
print("Average Item Price: Rp", average_item_price_8001)
print("Remainder: Rp", remainder_8001)

print("\n=== CUSTOMER ACCESS RIGHT ===")
print("Member Access:", member_access_8001)
print("Promo Access:", promo_access_8001)
print("Free Shipping Access:", free_shipping_access_8001)

print("\n=== OERATORS RESULTS ===")
Print("Arithmetic Operator: *, / , -, %")
print("Coparison Operator:", minimum_purchase_8001)
print("Logical Operator:", gets_discount_8001)
print("Assignment Operator - Points:", points_8001)
print("Membership Operator:", promo_availalable_8001)
print("Identify Operator:", same_identify_8001)
print("Bitwise AND:", check_member_8001)
print("Bitwise OR:", combined_status_8001)
print("Bitwise XOR:", difference_code_8001)

print("\n=== BITWISE OPERATIONS ===")
print("Transaction Status Code:", format(status_code_8001, "04b"))
print("Decimal Code:", status_code_8001)
print("Member Check:", format(check_member_8001, "04b"))
print("XOR Result:", format(difference_code_8001, "04b"))

print("\n=== DONE ===")


      


 
    

    