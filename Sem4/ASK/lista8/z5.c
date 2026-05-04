#include <stdio.h>




void proc(union elem *up)
{
    up->e2.x = *(up->e2.next->e1.p)- up->e2.next->e1.y)
}


/*proc:
12 movq 8(%rdi),%rax //w rdi mamy arguemnt (nasza unie) odwołuje sie jako dereferencja do drugiego elementu 
czyli u2 bo tam jest wskaznik
13 movq (%rax),%rdx // znowu dereferencja wiec u2.next wskazywało na u1.p
14 movq (%rdx),%rdx //dereferencjonujemy nasz *(up->e2.next->e1.p) i dostajemy wartosc liczbową
15 subq 8(%rax),%rdx //teraz odejmujemy od naszego zdereferencjonowanego wskaznika
//drugi element z e2->next, który musi byc wartoscią, czyli e1.y
16 movq %rdx,(%rdi)// i to wstawiamy na pierwszy element naszego argumentu czyli e2.x
17 ret
*/