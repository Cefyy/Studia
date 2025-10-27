#include <bits/stdc++.h>
using namespace std;

double metoda_polecenie(double x) {
    return std::pow(x, 3) + std::sqrt(std::pow(x, 6) + 2025);
}
double metoda_poprawiona(double x) {
    return 2025.0 / (std::sqrt(std::pow(x, 6) + 2025) - std::pow(x, 3));
}
int main()
{
    double test_values[] = {-10, -50, -100, -200, -500, -1000,-10000,-100000,-1000000};

    cout << setprecision(18);
     for (double x : test_values) {
        double polecenie_wynik = metoda_polecenie(x);
        double poprawiona_wynik = metoda_poprawiona(x);
        std::cout << std::setw(10) << x 
                  << std::setw(35) << polecenie_wynik
                  << std::setw(35) << poprawiona_wynik
                  << std::setw(25) << std::endl;
    }
}

