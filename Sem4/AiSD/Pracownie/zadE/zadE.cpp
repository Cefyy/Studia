#include <bits/stdc++.h>
using namespace std;

struct Field
{
    int h;
    int id;

    bool operator<(const Field &other) const
    {
        return h > other.h;
    }
};

struct Neighbour
{
    int row;
    int col;
};

const int maxFields = 1e6 + 5;
int parent[maxFields];
int above_sea[maxFields];
vector<Field> fields;
vector<int> queries;

int find(int v)
{
    if (v == parent[v])
    {
        return v;
    }
    return parent[v] = find(parent[v]);
}

void union_set(int a, int b, int &islands)
{
    a = find(a);
    b = find(b);
    if (a != b)
    {
        parent[b] = a;
        islands--;
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m, q;
    cin >> n >> m;
    int num_of_fields = n * m;
    fields.resize(num_of_fields + 1);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int h;
            cin >> h;
            int id = i * m + j;
            fields[id] = {h, id};
            parent[id] = id;
            above_sea[id] = false;
        }
    }
    cin >> q;
    queries.resize(q + 1);

    for (int i = 0; i < q; i++)
    {
        cin >> queries[i];
    }

    vector<int> results(q);
    int islands = 0, field_idx = 0;
    Neighbour neighbours[] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // d,u,l,r

    sort(fields.begin(), fields.end());

    for (int z = q - 1; z >= 0; z--)
    {
        int curr_level = queries[z];

        while (field_idx < num_of_fields && fields[field_idx].h > curr_level)
        {
            int id = fields[field_idx].id;

            int i = id / m;
            int j = id % m;

            above_sea[id] = true;
            islands++;

            for (int d = 0; d < 4; d++)
            {
                int n_row = i + neighbours[d].row;
                int n_col = j + neighbours[d].col;

                if (n_row >= 0 && n_row < n && n_col >= 0 && n_col < m)
                {
                    int neighbour_id = n_row * m + n_col;

                    if (above_sea[neighbour_id])
                    {
                        union_set(id, neighbour_id, islands);
                    }
                }
            }
            field_idx++;
        }
        results[z] = islands;
    }

    for (int i = 0; i < q; i++)
    {
        cout << results[i] << " ";
    }
}