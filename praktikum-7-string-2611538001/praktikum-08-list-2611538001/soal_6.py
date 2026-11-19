LAST_DIGIT = 1
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for i in range(7):
    amount = int(input(f"Day {i + 1}: "))
    expenses.append(amount)

total = 0
highest = expenses[0]
highest_day = 1
days_above_limit = 0

for i in range(7):
    total += expenses[i]

    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

    if expenses[i] > daily_limit:
        days_above_limit += 1

average = total / 7

print("Daily limit:", daily_limit)
print("Total expenses:", total)
print(f"Average expenses: {average:.1f}")
print("Highest expense: Day", highest_day, "-", highest)
print("Days above limit:", days_above_limit)
