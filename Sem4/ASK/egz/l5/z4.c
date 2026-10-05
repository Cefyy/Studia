int puzzle (long x,unsigned n)
{
    if(n==0)
    {
        return 0;
    }
    int result=0;
    for(unsigned i=0;i<n;i++)
    {
        result+=(x&1);
        x>>=1;
    }
    return result;


}