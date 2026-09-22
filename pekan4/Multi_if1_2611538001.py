umur_8001 = int(input("Input umur anda:"))
sim_8001 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_8001 >= 17 and sim_8001 == 'y':
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")

if umur_8001 >= 17 and sim_8001 != 'y':
    print("Anda Sudah Dewasa tetapi Tidak Boleh Bawa Motor")

if umur_8001 < 17 and sim_8001 == 'y':
    print("Anda Belum Cukup Umur Punya SIM")

if umur_8001 < 17 and sim_8001 != 'y':
    print("Anda Belum Cukup Umur Bawa Motor")