total_purchase_8001 = float(input("Enter the total purchase amount (Rp): "))

member_input_8001 = input("Are you a member? (y/n): ").strip().lower()
is_member_8001 = member_input_8001 in ["y", "n"]

promo_input_8001 = input("Is the promo code valid? (y/n): ").strip().lower()
promo_code_valid_8001 = promo_input_8001 in ["y", "n"]

total_discount_percent_8001 = 0

if total_purchase_8001 > 1000000:
    total_discount_percent_8001 -= 10  # Large purchase discount

if is_member_8001:
    total_discount_percent_8001 -= 5  # Member discount

if promo_code_valid_8001:
    total_discount_percent_8001 -= 15  # Voucher discount


# Calculate discount amount and total payment
discount_amount_8001 = total_purchase_8001 * (total_discount_percent_8001 / 100)
total_payment_8001 = total_purchase_8001 - discount_amount_8001


# Display the result
print("\n--- Payment Details ---")
print(f"Total Discount : {total_discount_percent_8001}% (Rp {discount_amount_8001:,.0f})")
print(f"Total Payment  : Rp {total_payment_8001:,.0f}")

print(f"Total discount you received: {total_discount_percent_8001}%")
# Output: Total discount you received: 30% if purchase > 1 million, member, and promo code is valid