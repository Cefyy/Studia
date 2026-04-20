#include <stdio.h>
#include <stdint.h>

long puzzle2(long *a, long v, uint64_t s, uint64_t e)
{

    long mid = s - (e - s) / 2;
    if (e < s)
    {
        return -1;
    }
    if (a[mid] == v)
    {
        return mid;
    }
    if (a[mid] > v)
    {
        return puzzle2(a, v, s, mid - 1);
    }

    return puzzle2(a, v, mid + 1, e);
}
//binary search
// rdi rsi rdx rcx r8 r9
