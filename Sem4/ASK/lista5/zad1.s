
.globl add_x_y

add_x_y:
    movq %rsi, %rax
    addq %rcx, %rax
    adcq %rdi, %rdx

    ret
