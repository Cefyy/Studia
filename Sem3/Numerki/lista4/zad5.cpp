#include <bits/stdc++.h>
using namespace std;




void newton(double x0,double R)
{
    double eps = 1e-16;
    double xn = x0;
    double alpha = 0;
    int iteracje=0;
    while(true)
    {
        alpha = xn*(2.0-xn*R);
        iteracje++;
        if(fabs(xn-alpha)<eps)
        break;
        else
        xn=alpha;
    }

    cout << "Otrzymano wynik: " << alpha << " po " << iteracje << " iteracjach\n";
}

int main()
{
    double Rs[5]={0.5,2.0,10.0,123.456,1.0};
    double x0[10]={1.0,0.5,0.1,0.05,0.05,0.09,0.005,0.008,0.1,0.001};
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<2;j++)
        {
            cout << "R: " << Rs[i] << " x0: " << x0[2*i+j] << " ";
            newton(x0[2*i+j],Rs[i]);
        }
    }
}