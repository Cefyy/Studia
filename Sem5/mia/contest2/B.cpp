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
        vector<int> gora(n, 0);
        for (int i = 0; i < n; i++)
        {
            cin >> gora[i];
        }
        vector<pair<int, int>> pary;
        int max_min = -999999;
        int max_min_idx = 0;
        int res = 0;
        for (int i = 0; i < n; i++)
        {
            int a;
            cin >> a;
            pary.push_back({gora[i], a});
            if (min(a, gora[i]) > max_min)
            {
                max_min = min(a, gora[i]);
                max_min_idx = i;
            }
        }
        for (int i = 0; i < n; i++)
        {
            if (i == max_min_idx)
            {
                res += pary[i].first + pary[i].second;
            }
            else
            {
                if (pary[i].first > pary[i].second)
                {
                    res += pary[i].first;
                }
                else
                {
                    res += pary[i].second;
                }
            }
        }
        cout << res << endl;
    }
}