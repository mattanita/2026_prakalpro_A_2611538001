menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# Read sales data
for day in range(number_of_days):
    row = []

    for menu in menus:
        portions = int(input(f"Day {day + 1}, {menu}: "))
        row.append(portions)

    sales.append(row)

# Calculate total portions per day
print("Total per day:")

for i in range(number_of_days):
    total = 0

    for portions in sales[i]:
        total += portions

    print(f"Day {i + 1}: {total}")

# Calculate total portions per menu
menu_totals = []

for j in range(len(menus)):
    total = 0

    for i in range(number_of_days):
        total += sales[i][j]

    menu_totals.append((menus[j], total))

print("Total per menu:", menu_totals)

# Find the best-selling menu
best_name, best_total = menu_totals[0]

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print("Best seller:", best_name, f"({best_total})")