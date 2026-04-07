#include <bits/stdc++.h>
using namespace std;

const int SZ = 1e6 + 1;
int n;
vector<int> dane;
int total_sum = 0;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    dane.resize(n);

    for (int i = 0; i < n; i++)
    {
        cin >> dane[i];
        total_sum += dane[i];
    }
    vector<int> dp(total_sum + 1, -1);
    vector<int> next_dp(total_sum + 1, -1);
    dp[0] = 0;
    int curr_sum = 0;
    for (int i = 0; i < n; i++)
    {
        int h = dane[i];
        for (int d = 0; d <= curr_sum; d++) // nie uzywamy klocka h
        {
            next_dp[d] = dp[d];
        }
        for (int d = curr_sum + 1; d <= curr_sum + h; d++) // czyscimy stare dane
        {
            next_dp[d] = -1;
        }
        for (int d = 0; d <= curr_sum; d++)
        {
            if (dp[d] == -1)
                continue;

            int new_d = d + h;

            next_dp[new_d] = max(next_dp[new_d], dp[d] + h);

            if (d >= h)
            {
                int new_d1 = d - h;
                next_dp[new_d1] = max(next_dp[new_d1], dp[d]);
            }
            else
            {
                int new_d2 = h - d;
                next_dp[new_d2] = max(next_dp[new_d2], dp[d] + h - d);
            }
        }
        curr_sum += h;
        swap(dp, next_dp);
    }
    if (dp[0] > 0)
    {

        cout << "TAK\n"
             << dp[0];
    }
    else
    {
        cout << "NIE" << "\n";
        for (int d = 1; d <= total_sum; d++)
        {
            if (dp[d] > d)
            {
                cout << d;
                break;
            }
        }
    }
}