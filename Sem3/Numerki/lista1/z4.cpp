#include <bits/stdc++.h>
using namespace std;
//nie są wiarygodne bo y(n) = (-1/9)^n
// Dowód przez wolframalpha tak powiedział

int main()
{
    double y[55];
    y[0]=1;
    y[1]=-1.0/9.0;
    for(int i=2;i<=50;i++)
    {
        y[i]=98.0*y[i-1]/9.0+11.0*y[i-2]/9.0;
        cout << setprecision(18) << "i="<< i << ": " <<y[i] << endl;
    }
    
}