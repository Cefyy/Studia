#include <stdio.h>

long pointless(long n, long *p)
{
    long local_var; 
    // w funkcji nadpisujemy rejestry r14 i rbx dlatego wrzucamy ich wartosci na stack zeby je uratowac (calee saved)
    // wrzucenie na stack rax powoduje przesuniecie rsp o adres w dół zeby zdobyc wskaznik na local_var które jest pozniej uzywane jako argument funkcji
    long result;

    if(n<=0)
    {
        result = 0;
    }
    else
    {
        result = pointless(n*2,&local_var) + local_var;
    }
    *p = n + result;
    return result;
}
// rejest powrotu znajduje sie na samej górze rekordu aktywacji i wrzuca go niejawnie call
// zapisane rejestry: calee saved r14 i rbx
// zmienna lokalna 8 bajtowa najnizszy adres w rekordzie aktywacji


//Standard ABI wymusza by przed wykoanniem call wskaznik rsp był podzielny przez 16
//call pointless odkłada adres powrotu -8 czyli %16 = 8
// oddkładamy trzy rejestry czyli -24 %16 = 0

// czemu zdecydowano sie na taką konwencje?
// ze względu na to ze w niektórych instrukcjach dane muszą byc wyrównywane do 16 bajtów
