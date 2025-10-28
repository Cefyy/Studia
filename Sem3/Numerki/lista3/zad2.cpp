#include <bits/stdc++.h>
using namespace std;

void metoda_delta(double a, double b, double c) {
    double delta = b * b - 4.0 * a * c;
    double x1 = (-b - sqrt(delta)) / (2.0* a);
    double x2 = (-b + sqrt(delta)) / (2.0 * a);
    cout << x1 << " " << x2 << endl;
}

void metoda_viete(double a, double b, double c){
    double delta = b * b - 4 * a * c;
    double x1,x2;
    if(b>=0)
    {
        x1 = (-b - sqrt(delta)) / (2.0 * a);
        x2 = c / (a * x1);
    }
    else
    {
        x2 = (-b + sqrt(delta)) / (2.0 * a);
        x1 = c / (a * x2);
    }
    cout << x1 << " " << x2 << endl;
}

int main(){
    double a = 0.000000001;
    double b = 1000000000;
    double c = 0.000000001;
    // powinno być
    // x1 = -10^18 
    // x2 = -1*10^-18
    metoda_delta(a, b, c);
    metoda_viete(a, b, c);
    return 0;
}