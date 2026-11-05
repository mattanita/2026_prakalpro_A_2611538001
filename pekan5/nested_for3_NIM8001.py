# This program uses the input() functoin

limit = int(input("Enter the limit value: "))
for i in range(limit+1):
    for j in range(limit+1):
        print(i+j, end=" ")
    print()    # move to the next line