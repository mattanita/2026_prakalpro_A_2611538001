# This program uses the input() function

height = int(input("Enter pattern height (even number , e.g. 10): "))

if height % 2 != 0:
    print("Height must be an even number!")
else:
    a = height
    c = awidth = (2 * height) - 2

    for i in range(1, height + 1):
        b = c + 1

        for j in range(1, height + 1):

            # Top  and bottom rows
            if i == 1 or i == height:
                if j == 1 or j == awidth:
                    print("#", end="")
                else:
                    print("=", end="")

            # Content rows
            else:
                if j == 1 or j == awidth:
                    print("|", end="")
                else:
                    if j == c:
                        print("<", end=" ")
                    elif j == b:
                        print(">", end=" ")
                    elif j == (awidth - c):
                        print("<", end=" ")
                    elif j == (awidth - c +1):
                        print(">", end=" ")
                    elif j > b and j< (awidth - c):
                        print(".", end=" ")
                    else:
                        print(" ", end=" ")

        print()

        # Original Java logic
        a -= 2

        if a <= 0:
            c = (-a) + 2
        else:
            c  = a
