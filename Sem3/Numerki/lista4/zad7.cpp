#include <bits/stdc++.h>
using namespace std;


double newton_sqrt_m(double m, double x0) {
    const double eps = 1e-16;
    const int MAX_IT = 1000;
    double x = x0;
    for (int i = 0; i < MAX_IT; i++) {
        double x_next = 0.5 * (x + m / x);
        if (fabs(x_next - x) < eps * fabs(x_next))
            return x_next;
        x = x_next;
    }
    return x;
}


void sqrt_decomposed(double a, double x0)
{
    if (a <= 0.0) {
        cout << "a musi byc dodatnie!\n";
        return;
    }


    int c;                         
    double m = frexp(a, &c);        


    if (c % 2 != 0) {               
        m *= 2.0;
        c -= 1;
    }


    double sqrt_m = newton_sqrt_m(m, x0);

    double result = ldexp(sqrt_m, c / 2); 


    cout << fixed << setprecision(15);
    cout << "a = " << setw(10) << a
         << ", m = " << setw(10) << m
         << ", c = " << setw(4) << c
         << ", x0 = " << setw(10) << x0
         << "  -> wynik: " << setw(15) << result
         << "  (sqrt(a) = " << sqrt(a) << ")\n";
}

int main()
{
    cout << "=== Zadanie 4.7: sqrt(a) z rozkladem na mantyse i ceche ===\n\n";

    double a1 = 4.0;
    double a2 = 50.0;



    cout << "--- Wyniki dla a = 4.0 ---\n";
    sqrt_decomposed(a1, -1.5); 
    sqrt_decomposed(a1, 0.5);    
    sqrt_decomposed(a1, 2.0);    

    cout << "\n--- Wyniki dla a = 50.0 ---\n";
    sqrt_decomposed(a2, -10.0);
    sqrt_decomposed(a2, 3.0);    
    sqrt_decomposed(a2, 10.0); 


    //Wniosek dla x<0 otrzymujemy wynik na minusie, a dla x>0 nie wazne czy wiekszy czy mniejszy od wyniku to zbiega on do wyniku
    return 0;
}
