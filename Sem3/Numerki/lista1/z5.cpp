#include <bits/stdc++.h>
using namespace std;


int main()
{
    double wyniki[25];
    double wynikIn=log(2026.0/2025.0);
    wyniki[0]=wynikIn;
    for(int i=1;i<=20;i++)
    {
        wynikIn = 1.0/i - 2025*wynikIn;
        wyniki[i]=wynikIn;
    }
    for(int i=0;i<=20;i+=2)
    {
        cout << "#" << i << ": " << wyniki[i] << endl;
    }
    for(int i=1;i<=20;i+=2)
    {
        cout << "#" << i << ": " << wyniki[i] << endl;
    }
}