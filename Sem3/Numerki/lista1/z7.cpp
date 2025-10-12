#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;


int main()
{
    double suma=1.0;
    double krok=1.0;
    double sign = 1.0;

    double x;
    int k=0;
    cin >> x;

    if(x < 0)
    {
        x*=-1.0;
    }
    if(x > M_PI_2)
    {
        x=M_PI-x;
        sign=-1.0;
    }

    while(fabs(krok)>1e-16)
    {
        k++;
        krok=krok = -krok * (x*x) / ((2.0*k)*(2.0*k - 1.0));
        suma+=krok;
    }
    suma*=sign;
    cout << setprecision(40) << fabs(suma-sign*cos(x));
}