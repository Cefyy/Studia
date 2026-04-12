#include <stdio.h>

int puzzle(long x, unsigned n)
{
    if (n == 0) //%testl (w asm jesli wyjdzie wynik zero przy andowaniu to ZF sie ustawi na 1 i to sprawdza je)
    {
        return 0; //L4 ret
    }
    int result = 0;  // eax
    int counter = 0; // edx
    while (result < n) //cmp i jne w L3
    {
        int c = x; //%movl %edi,%ecx
        c = x & 1; // w ecx (c) bedzie albo 1 albo 0 w zaleznosci od tego czy ostatni bit był zapalony
        result += c; //addl %ecx,%eax
        x = x >> 1; //sarq %rdi
        counter++; //incl %edx
    }
    return result; // l3 ret
}