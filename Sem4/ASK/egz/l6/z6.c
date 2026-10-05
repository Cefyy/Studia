long puzzle6(void)
{
    long dzielna,dzielnik;
    readlong(&dzielna);
    readlong(&dzielnik);
    long res = dzielna%dzielnik;
    return(res==0);
    
}

long readlong(long *p)
