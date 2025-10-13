#include <bits/stdc++.h>
using namespace std;


int main()
{

    double wynikIn=log(2026.0/2025.0);
    for(int i=1;i<=20;i++)
    {
        wynikIn = 1.0/i - 2025*wynikIn;
        cout << setprecision(18) << "#" << i << ": " << wynikIn << endl;
    }
}