#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios_base::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);
    long long n;
    cin >> n;
    vector<long long> nums(n,0);
    long long sum=0;
    for(int i=0;i<n;i++)
    {
        cin >> nums[i];
        sum+=nums[i];
    }

    vector<long long> sum_wo(n,0);
    for(int i=0;i<n;i++)
    {
        sum_wo[i]=sum-nums[i];
    }
    int z;
    cin >> z;
    while(z--)
    {
        long long x,y;
    cin >> x >> y;


    long long minimum = LONG_LONG_MAX;
    for(int i=0;i<n;i++)
    {
        long long curr = 0;
        if(y > sum_wo[i])
        {
            curr+=(y-sum_wo[i]);
        }
        if(x > nums[i])
        {
            curr+=(x-nums[i]);
        }
        if(curr < minimum)
        {
            minimum=curr;
        }
    }
    cout << minimum << endl;

    }
}