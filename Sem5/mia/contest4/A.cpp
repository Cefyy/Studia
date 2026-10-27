#include <bits/stdc++.h>
using namespace std;

void solve()
{
    string s;
    cin >> s;
    if (s!="()")
    {
        cout << "YES" << endl;
        string s1="",s2="";
        for(int i=0;i<s.size();i++)
        {
            s1+="()";
        }
        for(int i=0;i<s.size();i++)
        {
            s2+='(';
        }
        for(int i=0;i<s.size();i++)
        {
            s2+=')';
        }

        if(s1.find(s)!= string::npos)
        {
            cout << s2 << endl;
        }
        else
        {
            cout << s1 << endl;
        }
    }
    else
    {
        cout << "NO" << endl;
    }
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