#include <bits/stdc++.h>
using namespace std;

int binary_search(int n, vector<int> &uq, int x)
{
    int start = 0;
    int end = n - 1;
    while (start <= end)
    {
        int mid = (start + end) / 2;

        if (x == uq[mid])
        {
            return mid;
        }
        if (x > uq[mid])
        {
            start = mid + 1;
        }
        if (x < uq[mid])
        {
            end = mid - 1;
        }
    }
    return -1;
}
int create_ranks(vector<int> &carts, int n, vector<int> &ranks)
{
    vector<int> copy = carts;
    vector<int> uq;
    sort(copy.begin(), copy.end());
    uq.push_back(copy[0]);
    for (int i = 1; i < n; i++)
    {
        if (copy[i] != copy[i - 1])
        {
            uq.push_back(copy[i]);
        }
    }
    int uq_size = uq.size();
    for (int i = 0; i < n; i++)
    {
        
        ranks[i] = binary_search(uq_size, uq, carts[i]);
    }
    return uq_size;
}

void update_tree(int pos, int val, int N, vector<int> &tree)
{
    pos += N;
    if (val > tree[pos])
    {
        tree[pos] = val;
        pos /= 2;
        while (pos > 0)
        {
            tree[pos] = max(tree[2 * pos], tree[2 * pos + 1]);
            pos /= 2;
        }
    }
}
int query_tree(int l, int r, int N, vector<int> &tree)
{
    l += N;
    r += N;
    int res = 0;
    while (l <= r)
    {
        if (l % 2 == 1)
            res = max(res, tree[l++]);
        if (r % 2 == 0)
            res = max(res, tree[r--]);
        l /= 2;
        r /= 2;
    }
    return res;
}
int solve(vector<int> &carts, int n)
{
    int result = 1;

    vector<int> left(n, 0);  // left[i] - najdluzszy rosnacy pociag konczacy sie w i-tym wagonie
    vector<int> right(n, 0); // right[i] - najdluzszy rosnacy pociag zaczynajacy się w i-tym wagonie
    left[0] = 1;
    right[n - 1] = 1;
    for (int i = 1; i < n; i++)
    {
        if (carts[i] > carts[i - 1])
        {
            left[i] = left[i - 1] + 1;
            result = max(result, left[i]);
        }
        else
        {
            left[i] = 1;
        }
    }
    for (int i = n - 2; i >= 0; i--)
    {
        if (carts[i] < carts[i + 1])
        {
            right[i] = right[i + 1] + 1;
        }
        else
        {
            right[i] = 1;
        }
    }
    vector<int> ranks(n, 0);
    int uq_size = create_ranks(carts, n, ranks);
    int N = 1;
    while (N < uq_size)
        N <<= 1;
    vector<int> tree(2 * N, 0);
    for (int j = 0; j < n; j++)
    {
        int r = ranks[j];
        if (r > 0)
        {
            int best_left = query_tree(0, r - 1, N, tree);
            if (best_left > 0)
            {
                result = max(result, best_left + right[j]);
            }
        }
        update_tree(r, left[j], N, tree);
    }

    return result;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int q;
    cin >> q;

    while (q--)
    {
        int n;
        cin >> n;
        vector<int> carts(n, 0);
        for (int i = 0; i < n; i++)
        {
            cin >> carts[i];
        }
        cout << solve(carts, n) << "\n";
    }
}
