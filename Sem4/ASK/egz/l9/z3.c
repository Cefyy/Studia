void compute2(long *a, long *b, long k)
{
    long n = 1 << k;
    for (long i = 0; i < n; i++)
        a[i * n] = a[i] = 0;
    for (long i = 1; i < n; i++)
     {   long ni = i*n;
        for (long j = 1; j < n; j++)
          {  
            long nij=ni+j;
            a[nij] = i * j;
            b[nij] = i*j + (i-1)*(j-1);
          }
        }
}