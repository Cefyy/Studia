#include <stdio.h>


void compute2(long *a, long *b, long k) {
 long n = 1 << k;
    for (long i = 0; i < n; i++)
        a[i * n] = a[i] = 0;


    for (long i = 1; i < n; i++)
        for (long j = 1; j < n; j++)
            a[j * n + i] = i * j;


    for (long i = 1; i < n; i++)
        for (long j = 1; j < n; j++)
            b[i * n + j] = a[i * n + j] + a[(i - 1) * n + (j - 1)];
 }