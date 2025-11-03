#include <bits/stdc++.h>
using namespace std;

double f(double x){
    return x-0.49;
}
int main()
{
    double alpha = 0.49;
    double a0 = 0.0;
    double b0 = 1.0;


    double a=a0;
    double b=b0;
    cout << fixed << setprecision(12);
    cout << "n\ta_n\t\t\tb_n\t\t\tm_{n+1}\t\t\te_n\t\t\testimated error\n";

    for(int i=1;i<=5;i++)
    {
        double m = 0.5*(a+b);
        if(f(a)*f(m)<=0)
        {
            b=m;
        }
        else
        {
            a=m;
        }
        double mn1 = 0.5*(a+b);
        double en = alpha - mn1;
        double err_estimated = pow(2.0,-i-1.0)*(b0-a0);
        cout << i << "\t"
             << a << "\t\t" << b << "\t\t"
             << mn1 << "\t\t"
             << en << "\t\t" << err_estimated << "\n";
    }
}