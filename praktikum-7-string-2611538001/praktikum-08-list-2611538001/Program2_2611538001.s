# Nama: Matt Anita
# NIM: 2611538001
# Program Penjumlahan Dua Bilangan

.data
msg_title: .asciiz "Penjumlahan dua Bilangan\n"
val_a: .word 100
val_b: .word 50
res_val: .word 0

.text
.globl main

main:
    # Cetak Judul
    li $v0, 4
    la $a0, msg_title
    syscall

    # Muat data dari memori ke register
    lw $t0, val_a
    lw $t1, val_b

    # Eksekusi penjumlahan
    addu $t2, $t0, $t1
    sw $t2, res_val

    # Cetak Hasil
    li $v0, 1
    move $a0, $t2
    syscall

    # Keluar dari Program
    li $v0, 10
    syscall