#include <bits/stdc++.h>
using namespace std;




void newton(double x0,double a)
{
    double eps = 1e-16;
    double xn = x0;
    double alpha = 0;
    int iteracje=0;
    while(true)
    {
        alpha = (0.5*xn)*(3.0-xn*xn*a);
        iteracje++;
        if(fabs(xn-alpha)<eps)
        break;
        else
        xn=alpha;
    }

    cout << setprecision(16) <<  "Otrzymano wynik: " << left << setw(20) << alpha << " po " << iteracje << " iteracjach\n";
}

int main()
{
    double As[5]={4.0,0.16,256.0,0.0001,1.0}; //1/2, 1/0.4=2.5 1/16=0.0625,1/0.01=100,1
    double x0[10]={0.45,0.25,2.4,1.5,0.05,0.0125,95,20,0.95,0.25};
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<2;j++)
        {
            cout << "a: " <<left << setw(6) << As[i]  << " x0: " << left << setw(6) << x0[2*i+j] << " ";
            newton(x0[2*i+j],As[i]);
        }
    }
}