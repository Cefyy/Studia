#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;



double metoda_polecenie(double x) {
    double x_3 = x*x*x;
    return (M_PI_2 - x - atan(1.0/x))/x_3;
}

double metoda_poprawiona(double x) {
    double x_2=x*x;
    double x_4=x_2*x_2;
    double x_6=x_4*x_2;
    double x_8=x_4*x_2;
    return -1.0/3.0 + x_2/5.0 -  x_4/7.0 + x_6/9.0 - x_8/11.0;
}

int main()
{
    double test_values[] = {0.00000001,0.0000001,0.0000005,0.000001,0.0000001,0.00001,0.0001,0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5};

    cout << setprecision(18);
     for (double x : test_values) {
        double polecenie_wynik = metoda_polecenie(x);
        double poprawiona_wynik = metoda_poprawiona(x);
        std::cout << std::setw(30) << x 
                  << std::setw(35) << polecenie_wynik
                  << std::setw(35) << poprawiona_wynik
                  << std::setw(25) << std::endl;
    }
}

