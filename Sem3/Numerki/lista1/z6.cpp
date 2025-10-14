#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;


int main()
{
    double sumad=0;
    float sumaf=0;

    for(int i=0;i<=1999999;i++)
    {
        if(i%2==0)
        {
            sumad+=double(4.0/(2.0*i+1.0));
            sumaf+=float(4.0/(2.0*i+1.0));
        }
        else
        {
            sumad-=double(4.0/(2.0*i+1.0));
            sumaf-=float(4.0/(2.0*i+1.0));
        }
    }
    cout << setprecision(18) <<"wynik dla arytmetyki podwojnej: " << sumad << endl <<"wynik dla arytmetyki pojedynczej: " << sumaf;
}