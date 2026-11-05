# This program uses the input() function

repeat = int(input("Enter the number of repetition: "))

total = 0
for i in range(1, repeat + 1) :
    print(i, end=" ")
    total = total + i

    if i < repeat:
        print(" + ", end=" ")
    else:
        print(" = ", total, end=" ")
print()
print("Total =", total)