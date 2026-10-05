.L2:
movb 1(%rdi), %al
testb %al, %al
je .L6
movb (%rdi), %dl
cmpb %al, %dl
jle .L3
movb %al, (%rdi)
movb %dl, 1(%rdi)
.L3:
incq %rdi
jmp .L2
.L6:
ret