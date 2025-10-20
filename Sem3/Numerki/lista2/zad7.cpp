#include <bits/stdc++.h>
using namespace std;

double f1(double x)
{
    return (sqrt(12150.0*pow(x,15.0)+9.0)-3.0)/pow(x,15.0);
}
double f2(double x)
{
    return (12150.0/(sqrt(12150.0*pow(x,15.0)+9.0)+3.0));
}
int main()
{
    double x = 0.01;
    cout << fixed << setprecision(16) << f1(x) << " " << f2(x);
}