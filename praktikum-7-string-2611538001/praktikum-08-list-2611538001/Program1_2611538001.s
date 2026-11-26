# Nama: Matt Anita
# NIM: 2611538001

.data
pesan: .asciiz "Halo, World"

.text
.globl main

main:
    # Menampilkan teks ke layar konsol
    li $v0, 4
    la $a0, pesan
    syscall

    # Mengakhiri program
    li $v0, 10
    syscall