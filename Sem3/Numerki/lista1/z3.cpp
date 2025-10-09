//dla wiekszych liczn
#include <bits/stdc++.h>
using namespace std;

double fd(double x)
{
    return ((162.0*(1.0-cos(5.0*x)))/(x*x));
}
float ff(float x)
{
    return ((162.0*(1.0-cos(5.0*x)))/(x*x));
}

int main()
{
    for(double i=1;i<=20;i++)
    {
        cout <<setprecision(40) << "Wartosci dla i = " << i << " " <<"double: " <<fd(pow(10,-i)) << " single: "<< ff(float(pow(10,-i))) << endl;
    }
}