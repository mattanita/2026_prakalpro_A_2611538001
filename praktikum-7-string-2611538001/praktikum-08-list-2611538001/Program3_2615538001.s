# Nama: Matt Anita
# NIM: 2611538001
# Program Penjumlahan Data Array

.data
array_data: .word 10, 20, 30, 40, 50
size: .word 5
msg_in: .asciiz "Input : "
msg_out: .asciiz "\nOutput : "
spasi: .asciiz " "

.text
.globl main

main:
    la $s0, array_data
    lw $s1, size

    # Tampilkan data awal
    li $v0, 4
    la $a0, msg_in
    syscall

    li $t0, 0

loop_input:
    beq $t0, $s1, mulai_proses
    sll $t1, $t0, 2
    addu $t2, $s0, $t1

    lw $a0, 0($t2)
    li $v0, 1
    syscall

    li $v0, 4
    la $a0, spasi
    syscall

    addiu $t0, $t0, 1
    j loop_input

mulai_proses:
    li $v0, 4
    la $a0, msg_out
    syscall

    li $t0, 0

loop_output:
    beq $t0, $s1, loop_end
    sll $t1, $t0, 2
    addu $t2, $s0, $t1
    lw $t3, 0($t2)

    # Tambah 5
    addiu $t3, $t3, 5
    sw $t3, 0($t2)

    # Cetak hasil
    move $a0, $t3
    li $v0, 1
    syscall

    li $v0, 4
    la $a0, spasi
    syscall

    addiu $t0, $t0, 1
    j loop_output

loop_end:
    li $v0, 10
    syscall