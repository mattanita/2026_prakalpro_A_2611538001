limit = int(input("Enter the limit value: "))
for i in range(1, limit + 1):
    for j in range(1, limit + 1):
        print("*", end=" ")
    print()   # move to the next line