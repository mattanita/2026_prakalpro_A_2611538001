angka1_8001= int(input("Input angkat-1: "))
angka2_8001= int(input("Input angka-2: "))

#Penjumlahan
hasil = angka1_8001 + angka2_8001
print("\nOperator Penjumlahan")
print("Hasil=",hasil)

#Pengurangan
hasil = angka1_8001 - angka2_8001
print("\nOperator Pengurangan")
print("Hasil=", hasil)

#Perkalian
hasil = angka1_8001 * angka2_8001
print("\nOperator perkalian")
print("Hasil=", hasil)

#Pembagin, pembagian bulat, dan sisa bagi
if angka2_8001 !=0:
    hasil = angka1_8001 / angka2_8001
    print("\nOperator Pembagin")
    print("Hasil =", hasil)

    hasil = angka1_8001 // angka2_8001
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1_8001 % angka2_8001
    print("\nOpeerator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("Angka Kededua tidak boleh nol.")

    #Pangkat
    hasil = angka1_8001 ** angka2_8001
    print("\nOperator Pangkat")
    print("Hasil =", hasil)