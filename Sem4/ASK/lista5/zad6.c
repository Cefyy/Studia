#include <stdio.h>

long switch_prob(long x, long n)
{
    long result = x;
    switch(n)
    {
        case 60:
        case 61:
            result = 8*x; //lea 0x0(,%rdi,8), %rax
            break; //retq
        case 62:
            int rax = x*15; 
            /*
            movq %rdi, %rax przenosimy x do raxa
            shlq $0x4, %rax robimy x>>4 czyli x*16
            subq %rdi, %rax odejmujemy x czyli 16x - x = 15x;
            */
        case 65:
            x=x*x; //// imulq %rdi, %rdi break retq
        default: //ja *0x4005c3
            result = x+75; //leaq 0x4b(%rdi),%rax 75 + x + 0*0 do raxa
            break;
        case 64:
            result = x>>3;
            break;
    }
    return result;
}