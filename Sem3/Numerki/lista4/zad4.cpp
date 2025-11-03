#include <bits/stdc++.h>
//https://www.desmos.com/calculator?lang=pl 3x^{2}-5\cdot\cos\left(7x-1\right)
using namespace std;
double funkcja(double x){
    return 3.0*x*x - 5.0*cos(7.0*x-1);
}

double bisekcja(double a0, double b0) {
    double a = a0, b = b0, m;


    for (int i = 0; i < 19; ++i) {
        m = 0.5 * (a + b);

        if (funkcja(a) * funkcja(m) <= 0)
            b = m;
        else
            a = m;
    }

    return 0.5 * (a + b);
}

int main()
{
    //z wykresu wychodzi 6 zer
    cout << setprecision(16)
    << bisekcja(-1.3,-0.60) << endl
     << bisekcja(-0.9,-0.2) << endl
     << bisekcja(-0.5,0.3) << endl
     << bisekcja(0,0.8) << endl
     << bisekcja(0.4,1.1) << endl
     << bisekcja(0.9,1.7);
}
