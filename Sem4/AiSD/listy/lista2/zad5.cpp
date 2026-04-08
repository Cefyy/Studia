#include <iostream>
#include <vector>
#include <list>
#include <queue>

using namespace std;

vector<int> znajdzNajwiekszyPodzbior(int n, int k, const vector<vector<int>> &adj)
{
    vector<int> stopien(n, 0);
    for (int i = 0; i < n; ++i)
    {
        stopien[i] = adj[i].size();
    }

    int aktualny_rozmiar = n;
    int max_dozwolony_stopien = aktualny_rozmiar - 1 - k;

    vector<list<int>> kubelki(n);

    vector<list<int>::iterator> pozycja_w_wezle(n);

    vector<bool> w_zbiorze(n, false);
    queue<int> do_usuniecia;

    for (int i = 0; i < n; ++i)
    {
        if (stopien[i] < k || stopien[i] > max_dozwolony_stopien)
        {
            w_zbiorze[i] = false;
            do_usuniecia.push(i);
        }
        else
        {
            w_zbiorze[i] = true;
            kubelki[stopien[i]].push_front(i);

            pozycja_w_wezle[i] = kubelki[stopien[i]].begin();
        }
    }

    // 3. Faza główna: Reakcja łańcuchowa
    while (!do_usuniecia.empty())
    {
        int u = do_usuniecia.front();
        do_usuniecia.pop();

        if (aktualny_rozmiar == 0)
            break;

        // KROK A: Lawina dolna (Aktualizacja sąsiadów)
        for (int x : adj[u])
        {
            if (w_zbiorze[x])
            {
                // O(1)
                kubelki[stopien[x]].erase(pozycja_w_wezle[x]);

                stopien[x]--;

                if (stopien[x] < k)
                {
                    w_zbiorze[x] = false;
                    do_usuniecia.push(x);
                }
                else
                {

                    kubelki[stopien[x]].push_front(x);
                    pozycja_w_wezle[x] = kubelki[stopien[x]].begin();
                }
            }
        }

        // KROK B: Zmniejszenie globalnego rozmiaru grupy
        aktualny_rozmiar--;

        int nowy_max_dozwolony = aktualny_rozmiar - 1 - k;
        int nielegalny_kubelek = nowy_max_dozwolony + 1;

        // KROK C
        if (nielegalny_kubelek >= 0 && nielegalny_kubelek < n)
        {
            for (int v : kubelki[nielegalny_kubelek])
            {
                w_zbiorze[v] = false;
                do_usuniecia.push(v);
            }

            kubelki[nielegalny_kubelek].clear();
        }
    }

    // 4. Zbieranie wyników
    vector<int> wynik;
    for (int i = 0; i < n; ++i)
    {
        if (w_zbiorze[i])
        {
            wynik.push_back(i);
        }
    }
    return wynik;
}

// Prosty kod testujący działanie algorytmu
int main()
{
    int n = 7;
    int k = 2; // Każdy musi mieć min. 2 znajomych i 2 nieznajomych
    vector<vector<int>> adj(n);

    // Funkcja pomocnicza dodająca krawędź
    auto dodaj_krawedz = [&](int u, int v)
    {
        adj[u].push_back(v);
        adj[v].push_back(u);
    };

    // Budujemy testowy graf
    dodaj_krawedz(0, 1);
    dodaj_krawedz(1, 2);
    dodaj_krawedz(2, 3);
    dodaj_krawedz(3, 0);

    dodaj_krawedz(4, 0);
    dodaj_krawedz(4, 1);
    dodaj_krawedz(4, 2);
    dodaj_krawedz(4, 3);
    dodaj_krawedz(4, 5);
    dodaj_krawedz(4, 6);
    dodaj_krawedz(5, 6);

    vector<int> wynik = znajdzNajwiekszyPodzbior(n, k, adj);

    cout << "Wierzcholki tworzace maksymalny podzbior: ";
    if (wynik.empty())
    {
        cout << "Pusty (nie ma takiej grupy)\n";
    }
    else
    {
        for (int v : wynik)
        {
            cout << v << " ";
        }
        cout << "\n";
    }

    return 0;
}