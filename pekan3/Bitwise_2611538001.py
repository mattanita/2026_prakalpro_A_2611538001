print("\n====================================")
print("3. BITWISE OPERATOR")
print("======================================")

number1 = int(input("Enter bitwise number-1: "))
number2 = int(input("Enter bitwise number-2: "))

print("\nNumbers in decimal and binary form")
print("\nNumber1 =", number1 "| binary =" bin(number1))
print("\nNumber2 =", number2 "| binary =" bin(number2))


# Bitwise AND
result = number1 & number2
print("\nBitwise AND (&)")
print(number1, "&", bin(result))
print("Binary result =", bin(result))
print("Binary result (8 bit) =", format(result, "08b"))

#  Bitwise OR
result = number1 | number2
print("\nBitwise OR (|)")
print(number1, "|", number2, "=", result)
print("Binary result =", bin(result))
print("Binary result (8 bit) =", format(result, "08b"))

# Bitwise XOR
result = number1 ^ number2
print("\nBitwise XOR (^)")
print(number1, "^", number2, "=", result)
print("Binary result =", bin(result))
print("Binary result (8 bit) =", format(result, "08b"))

# bitwise NOT
result = ~number1
print("\nBitwise NOT (~)")
print("~", number1, "=", result)
print("Binary tresult =", bin(result))
print("Binary result (8 bit) =", format(result, "08b"))

# Bitwise left shift
shift_amount = int(input("\nEnter number of bits to shift: "))

result = number1 << shift_amount
print("\nBiwise Left Shift (<<) ")
print(number1, "<<", shift_amount, "=", result)
print("Binary result =", bin(result))
print("Binary result (8 bit) =" format (result, "08b"))

# Bitwise right shift
result = number1 >> shift_amount
print("\nBitwise Right Shift (>>)")
print(number1, ">>", shift _amount, "=", result)
print("binary result =", bin(reselt))
print("Binary result (8 bit) =", format(result, "08b"))