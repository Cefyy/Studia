#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int MAX_N = 100005;

long long C; // Szukana odległość (używamy long long w razie gigantycznych wag)
long long global_result = 0;

vector<pair<int, long long>> graf[MAX_N];
bool usuniety[MAX_N];
int sub_size[MAX_N];

// Zwykła mapa (Drzewo Czerwono-Czarne) - gwarantowane zapytania w O(log K)
map<long long, int> mapa_odleglosci;

// --- KROK 1 i 2 (Bez zmian) ---
void oblicz_rozmiary(int u, int p) {
    sub_size[u] = 1;
    for (auto krawedz : graf[u]) {
        int v = krawedz.first;
        if (v != p && !usuniety[v]) {
            oblicz_rozmiary(v, u);
            sub_size[u] += sub_size[v];
        }
    }
}

int znajdz_centroid(int u, int p, int total_size) {
    for (auto krawedz : graf[u]) {
        int v = krawedz.first;
        if (v != p && !usuniety[v] && sub_size[v] > total_size / 2) {
            return znajdz_centroid(v, u, total_size);
        }
    }
    return u;
}

// --- KROK 3: Pomocniczy DFS (Bez zmian) ---
void zbierz_odleglosci(int u, int p, long long obecny_dystans, vector<long long>& zebrane) {
    if (obecny_dystans > C) return;
    zebrane.push_back(obecny_dystans);
    for (auto krawedz : graf[u]) {
        int v = krawedz.first;
        if (v != p && !usuniety[v]) {
            zbierz_odleglosci(v, u, obecny_dystans + krawedz.second, zebrane);
        }
    }
}

// --- KROK 4: Główna funkcja (Dziel i Zwyciężaj) ---
void centroid_decomposition(int start_node) {
    
    oblicz_rozmiary(start_node, -1);
    int centroid = znajdz_centroid(start_node, -1, sub_size[start_node]);

    // Zaczynamy od czystej mapy (dla pewności)
    mapa_odleglosci.clear(); 
    mapa_odleglosci[0] = 1; // Sam centroid

    for (auto krawedz : graf[centroid]) {
        int v = krawedz.first;
        long long waga = krawedz.second;

        if (!usuniety[v]) {
            vector<long long> dystanse_w_galezi;
            zbierz_odleglosci(v, centroid, waga, dystanse_w_galezi);

            // FAZA ZAPYTAŃ
            for (long long d : dystanse_w_galezi) {
                long long szukana = C - d;
                if (szukana >= 0) {
                    // UWAGA: Używamy .count() zamiast samego mapa_odleglosci[szukana]
                    // To zapobiega tworzeniu "pustych" węzłów w drzewie czerwono-czarnym!
                    if (mapa_odleglosci.count(szukana)) {
                        global_result += mapa_odleglosci[szukana];
                    }
                }
            }

            // FAZA AKTUALIZACJI
            for (long long d : dystanse_w_galezi) {
                mapa_odleglosci[d]++;
            }
        }
    }

    // --- FAZA SPRZĄTANIA (Ogromna zaleta mapy!) ---
    // Nie potrzebujemy już trzeciego przejścia DFS!
    // Skoro w mapie są tylko elementy z aktualnego poddrzewa (którego rozmiar to K),
    // to metoda .clear() usunie wszystko w czasie O(K). 
    // To idealnie mieści się w naszym budżecie czasowym.
    mapa_odleglosci.clear();

    usuniety[centroid] = true;

    for (auto krawedz : graf[centroid]) {
        int v = krawedz.first;
        if (!usuniety[v]) {
            centroid_decomposition(v);
        }
    }
}