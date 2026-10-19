#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n,s;
    cin >> n >> s;
    int pos = 0;
    if(n%2==1)
    {
        pos = (n+1)/2;
    }
    else
    {
        pos = (n)/2;
    }

    int rest = n - (pos-1);
    cout << s/rest << endl;
}

int main()
{
    int z;
    cin >> z;
    while(z--)
    {
        solve();
    }
}