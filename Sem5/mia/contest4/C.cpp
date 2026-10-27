#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n,m,k;
    cin >> n >> m >> k;
    vector<int> nums(k,0);
    for(int i=0;i<k;i++)
    {
        cin >> nums[i];
    }
    int target = k;
    vector<bool> seen(k+1,0);
    int taken=0;
    for(int i=0;i<k;i++)
    {
        seen[nums[i]]=1;
        taken++;
        if(taken > n*m-3)
        {
            cout << "TIDAK" << endl;
            return;
        }
        while(seen[target])
        {
            target--;
            taken--;
        }

    }
    cout << "YA" << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int z;
    cin >> z;
    while (z--)
    {
        solve();
    }
}
