# Memasukkan nilai boolean.
# Input tidak peka terhadap huruf besar dan kecil.
a1_8001 = input("Input nilai boolean_1_8001 (true/false): ").strip().lower() == "true"
a2_8001 = input("Input nilai boolean_2_8001 (true/false): ").strip().lower() == "true"

print("\nA1_8001 =", a1_8001)
print("A2_8001 =", a2_8001)

# Konjungsi: bernilai True jika keduanya True.
hasil = a1_8001 and a2_8001
print("\nKonjungsi (AND)")
print("A1_8001 and A2_8001 =", hasil)

# Disjungsi: bernilai True jika salah satunya True.
hasil = a1_8001 or a2_8001
print("\nDisjungsi (OR)")
print("A1_8001 or A2_8001 =", hasil)

# Negasi A1_8001: membalik nilai A1_8001.
hasil = not a1_8001
print("\nNegasi A1_8001 (NOT)")
print("not A1_8001 =", hasil)

# Negasi A2_8001: membalik nilai A2_8001.
hasil = not a2_8001
print("\nNegasi A2_8001 (NOT)")
print("not A2_8001 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda.
hasil = a1_8001 != a2_8001
print("\nXOR")
print("A1_8001 xor A2_8001 =", hasil)





