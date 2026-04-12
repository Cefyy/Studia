#include <stdio.h>

long puzzle2(char *s, char *d)
{
    const char *curr_s = s; // movq %rdi,%rax

    for (;; curr_s++) // leaq 1(%rax),%r8;
    {
        const char* curr_d;
        //movb (%rdx), %cl;testb %cl, %cl;incq %rdx
        for (curr_d = d; *curr_d != '\0'; curr_d++)
        {
            if (*curr_d == *curr_s) //cmpb %cl, %r9b
            {
                break; 
                /*na odwrót logika bo w asm mamy jne .L2 czyli jak nie znajdziemy to wracamy do poczatku petli ale to robi za nas for,
                wiec po prostu wychodzimy gdy nie zadziała*/

            }
        }
        if(*curr_d == '\0') //je .L4
        {
            return curr_s-s;//.L4: subq %rdi, %rax ; ret

        }
    }
}