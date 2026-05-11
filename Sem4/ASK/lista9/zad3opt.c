void compute2(long *a, long *b, long k)
{
    long n = 1 << k;
    for (long i = 0; i < n; i++)
        a[i] = 0;

    for (long i = 1; i < n; i++)
    {
        long ni = n * i;
        for (long j = 1; j < n; j++)
        {
            long val = i*j;
            a[ni + j] = val;
            b[ni + j] = i + j -1;
        }
    }
}