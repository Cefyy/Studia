#include <bits/stdc++.h>
using namespace std;
int main()
{
        vector<double> vals;
    for (int e2 = 0; e2 <= 1; e2++)
    {
        for (int e3 = 0; e3 <= 1; e3++)
        {
            for (int e4 = 0; e4 <= 1; e4++)
            {
                for (int e5 = 0; e5 <= 1; e5++)
                {
                    double m = 0.5 + e2/4.0 + e3/8.0 + e4/16.0 + e5/32.0;
                    for(int c = 0;c<=1;++c)
                    {
                        double cecha = pow(2,c);
                    
                        for(int sign: {-1,1})
                        {
                            double val = sign*m*cecha;
                            vals.push_back(val);
                        }
                    }
                }
            }
        }
    }
    sort(vals.begin(),vals.end());
    vals.erase(unique(vals.begin(),vals.end()),vals.end());

    double A = vals.front();
    double B = vals.back();
    cout << fixed << setprecision(8);
    cout << "Wszystkie liczby: \n";
    for(double v : vals)
    {
        cout << setw(10) << v << endl;
    }

    cout << "Przedzial [A,B]: " << A << " " << B << endl;
}