
# this program usess the input() function

limit = int(input("Enter the limit value: "))
for line in range(1, limit + 1):
    for j in range(1, (-1 * line + limit) + 1):
        print(".", end=" ")
        print(line)

