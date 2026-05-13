#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 5;
vector<int> dane;
vector<int> A;
int dp[N][N];
int n, m;

int solve()
{
    for (int i = 0; i < n + 2; i++)
    {
        dp[i][i] = 0;
    }
    for (int i = 1; i < n + 2; i++)
    {
        dp[i - 1][i] = 0;
    }
    for (int k = 2; k < n + 2; k++) // j-i=2,3,4....
    {

        for (int i = 0, j = i + k; j < n + 2; j++, i++)
        {

            int result = 1e9 + 9;
            for (int z = i + 1; z < j; z++)
            {
                result = min(result, dp[i][z] + dp[z][j] + (A[j] - A[i]));
            }
            dp[i][j] = result;
        }
    }
    return dp[0][n + 1];
}

int main()
{
    cin >> n >> m;
    dane.resize(n);
    A.resize(n + 2);
    for (int i = 0; i < n; i++)
    {
        cin >> dane[i];
    }
    sort(dane.begin(), dane.end());
    A[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        A[i] = dane[i - 1];
    }
    A[n + 1] = m;
    cout << solve();
}
