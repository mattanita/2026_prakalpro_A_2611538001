
phone = "0812345678"
masked = "*" * (len(phone) - 4) + phone[-4:]
print(masked)