#include <bits/stdc++.h>
using namespace std;



int main()
{
    int z;
    cin >> z;
    while(z--)
    {
        int n;
        cin >> n;
        int max_beside_last=-1;
        for(int i=0;i<n-1;i++)
        {
            int a;
            cin >> a;
            max_beside_last=max(max_beside_last,a);

        }
        int last;
        cin >> last;
        cout << (last+max_beside_last) << endl;
    }
}
