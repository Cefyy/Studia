#include <bits/stdc++.h>
using namespace std;

double f1(double x)
{
    return (sqrt(12150*pow(x,15)+9)-3)/pow(x,15);
}
double f2(double x)
{
    return (12150/(sqrt(12150*pow(x,15)+9)+3));
}
int main()
{
    double x = 0.01;
    cout << fixed << setprecision(16) << f1(x) << " " << f2(x);
}