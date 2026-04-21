
void readlong(long *ptr);
long puzzle6(void)
{
    long dzielna;
    long dzielnik;
    //wyrównujemy do 16 bo na stosie jest return adress

    readlong(&dzielna);
    readlong(&dzielnik);
    long result = dzielna%dzielnik;
    return (result==0);
    

    //cofamy o 24 zostawiamy return adress

    

}