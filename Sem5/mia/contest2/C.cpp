#include <bits/stdc++.h>
using namespace std;

int main()
{
    int z;
    cin >> z;
    while (z--)
    {
        int n;
        cin >> n;
        map<int, int> wyst;
        for (int i = 0; i < n; i++)
        {
            int a;
            cin >> a;
            wyst[a]++;
        }
        map<int, int> wyst_count;
        for (auto &x : wyst)
        {
            wyst_count[x.second]++;
        }
        int res = n;
        int lewo=0,prawo=n,k=wyst.size();
        for(auto[x,y]: wyst_count)
        {
            res = min(lewo+prawo-k*x,res);
            lewo += x*y;
            prawo -= x*y;
            k-=y;
        }
        cout << res << endl;
        
        
        
    }
}