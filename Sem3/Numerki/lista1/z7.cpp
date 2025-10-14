#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;


int main()
{
    double suma=1.0;
    double krok=1.0;


    double x=M_PI/3;
    int k=0;

    if(x < 0)
    {
        x*=-1.0;
    }


    while(fabs(krok)>1e-16)
    {
        k++;
        krok=krok = -krok * (x*x) / ((2.0*k)*(2.0*k - 1.0));
        suma+=krok;
    }
    cout << setprecision(40) << "Moje Pi: " << suma << endl << "Biblioteczne Pi: " << cos(x);
}