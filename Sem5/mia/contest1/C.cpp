#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int z;
    cin >> z;
    while (z--)
    {
        int n, m;
        cin >> n >> m;
        vector<int> zero_c;
        vector<pair<int, int>> pos_c;
        multiset<int> swords;
        vector<int> monsters;
        for (int i = 0; i < n; i++)
        {
            int c;
            cin >> c;
            swords.insert(c);
        }
        for (int i = 0; i < m; i++)
        {
            int mon;
            cin >> mon;
            monsters.push_back(mon);
        }
        for (int i = 0; i < m; i++)
        {
            int c;
            cin >> c;
            if (c == 0)
            {
                zero_c.push_back(monsters[i]);
            }
            else
            {
                pos_c.push_back({monsters[i], c});
            }
        }
        sort(zero_c.begin(), zero_c.end());
        sort(pos_c.begin(), pos_c.end());
        int killed = 0;
        int pcsize = pos_c.size();
        for (int i = 0; i < pcsize; i++)
        {
            int hp = pos_c[i].first;
            auto cheapest_sword = swords.lower_bound(hp);
            if (cheapest_sword != swords.end())
            {
                killed++;
                int old_sword = *cheapest_sword;
                int new_sword = max(old_sword,pos_c[i].second);
                swords.erase(cheapest_sword);
                swords.insert(new_sword);
                

            }
            else
            {
                break;
            }
        }
        for (int i = 0; i < zero_c.size(); i++)
        {
            int hp = zero_c[i];
            auto cheapest_sword = swords.lower_bound(hp);
            if (cheapest_sword != swords.end())
            {
                killed++;
                swords.erase(cheapest_sword);
            }
            else
            {
                break;
            }
        }
        cout << killed << endl;
    }
}