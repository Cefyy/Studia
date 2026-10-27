#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n;
    cin >> n;
    vector<int> nums(n,0);
    for(int i=0;i<n;i++)
    {
        cin >> nums[i];
    }
    vector<int> mex_l(n,0);
    vector<int> mex_r(n,0);
    vector<bool> seen_l(n+1,false);
    vector<bool> seen_r(n+1,false);
    int mexl=0;
    for(int i=0;i<n;i++)
    {
        if(nums[i]<=n)
        {
            seen_l[nums[i]]=1;
        }
        while(seen_l[mexl])
        {
            mexl++;
        }
        mex_l[i]=mexl;
    }
    int mexr=0;
    for(int i=n-1;i>=0;i--)
    {
        if(nums[i]<=n)
        {
            seen_r[nums[i]]=1;
        }
        while(seen_r[mexr])
        {
            mexr++;
        }
        mex_r[i]=mexr;
    }
    for(int i=0;i<n-1;i++)
    {
        if(mex_l[i]==mex_r[i+1])
        {
            cout << 2 << "\n";
            cout << 1 << " " << i+1  << "\n" << i+2 << " " << n  << "\n";
            return;
        }
    }
    cout << -1 << endl;

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