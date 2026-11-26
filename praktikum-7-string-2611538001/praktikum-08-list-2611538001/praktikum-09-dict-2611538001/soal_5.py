n = int(input())
totals = {}

for _ in range(n):
  parts = input().split()
  name = parts[0]
  amount = int(parts[1])
  totals[name] = totals.get(name, 0) + amount

total_cash = sum(totals.values())

top_name = ""
top_amount = -1
for name, amount in totals.items():
  if amount > top_amount:
    top_amount = amount
    top_name = name

for name, amount in totals.items():
  print(f"{name}: {amount}")

print(f"Total cash: {total_cash}")
print(f"Top contributor: {top_name} ({top_amount})")