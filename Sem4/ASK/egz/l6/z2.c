long puzzle2(long *a,long v, uint64_t s, uint64_t e)
{
    long mid = (e-s)/2 + s;
    if(s == e)
    {
        return -1;
    }
    else
    {
        long temp = a[mid];
        if(v==temp)
        {
            return mid;
        }
        if(v > temp)
        {

            puzzle2(a,v,s,mid-1);
        }
        else
        {
            puzzle2(a,v,mid+1,e);
        }
    }


}
// rdi rsi rdx rcx