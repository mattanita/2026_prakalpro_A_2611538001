
umur = int(input("input umur anda: "))
sim = input("Apakah Anda Sudah Punya Sim c (y/t):")[0]

if umur >= 17 and sim == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur >= 17 and sim != "y":
    print("anda Sudah sewasa tetapi tidak boleh bawa motor")

if umur < 17 and sim == "y":
    print("anda Belum dewasa tetapi boleh bawa motor")

if umur < 17 and sim != "y":
    print("Anda Belum Cukup  Umur bawa motor")

if umur <17 and sim != "y":
    print("Anda Belum Cukup Umur bawa motor")

