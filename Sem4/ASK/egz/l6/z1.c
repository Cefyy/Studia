long pointless(long n,long *p)
{
    long local_var=0;
    long result=0;
    c=p;
    b=n;

    if(n==0)
    {
        result = 0;
    }
    else
    {
    result = pointless(2*n,&local_var) + local_var;
    *p = n + result;
    }
    return result;
    


}
// na samej górze return adress
// callee saved 2 zmienne
// local var


//zanim coś to musiało być podzielne przez 16
// call wrzuca return adress + 8
// trzy pushe + 24
// 0 mod 16 + 32 mod 16 = 0 mod 16 wszystko cacy