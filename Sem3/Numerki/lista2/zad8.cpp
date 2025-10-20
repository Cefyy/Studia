//dla komputera cos(5*10^-11) = cos(0) = 1 wiec 162*(1-1) = 0, 0/10^-22 to 0
//mozemy uzyc szeregu mclaurina do przyblizenia wartosci cos 
#include <bits/stdc++.h>
using namespace std;

double f_improv(double x)
{
    return (162*((25.0/2.0)-((625*x*x)/24.0) + (15625*x*x*x*x)/720.0));
}
double f(double x)
{
    return ((162*(1-cos(5*x)))/x*x);
}
int main()
{
    for(double i=5;i<=20;i++)
    {
        cout << fixed << setprecision(16);
        cout << f(pow(10.0,-i)) << " " << f_improv(pow(10.0,-i)) << endl;
    }
}


