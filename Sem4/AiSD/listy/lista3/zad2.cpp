#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Struktura reprezentująca punkt na płaszczyźnie
struct Point {
    long long x, y;
};

// Funkcja scalająca i zliczająca pary między dwiema połówkami
long long mergeAndCount(vector<Point>& pts, int left, int mid, int right) {
    int i = left;       // wskaźnik na początek lewej połowy (posortowanej po y)
    int j = mid + 1;    // wskaźnik na początek prawej połowy (posortowanej po y)
    long long count = 0;
    
    vector<Point> temp; // tymczasowa tablica do scalania
    temp.reserve(right - left + 1);

    // Przechodzimy przez obie połowy
    while (i <= mid && j <= right) {
        // Znaleźliśmy parę! (L[i].y < R[j].y)
        // Wiemy też z podziału, że L[i].x < R[j].x
        if (pts[i].y < pts[j].y) {
            // Skoro R jest posortowane rosnąco po y, to L[i] tworzy parę 
            // z R[j] oraz ze wszystkimi pozostałymi elementami w R.
            count += (right - j + 1);
            
            // Mniejszy element (z lewej) idzie do tablicy tymczasowej
            temp.push_back(pts[i]);
            i++;
        } else {
            // Brak ostrej dominacji, mniejszy/równy element (z prawej) idzie do temp
            temp.push_back(pts[j]);
            j++;
        }
    }

    // Przepisanie pozostałych elementów z lewej połowy
    while (i <= mid) {
        temp.push_back(pts[i]);
        i++;
    }

    // Przepisanie pozostałych elementów z prawej połowy
    while (j <= right) {
        temp.push_back(pts[j]);
        j++;
    }

    // Skopiowanie scalonej (posortowanej po y) tablicy z powrotem do oryginału
    for (int k = 0; k < temp.size(); ++k) {
        pts[left + k] = temp[k];
    }

    return count;
}

// Rekurencyjna funkcja Dziel i Zwyciężaj
long long countPairsRecursive(vector<Point>& pts, int left, int right) {
    long long count = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Liczymy pary całkowicie w lewej połowie
        count += countPairsRecursive(pts, left, mid);
        
        // Liczymy pary całkowicie w prawej połowie
        count += countPairsRecursive(pts, mid + 1, right);
        
        // Liczymy pary pomiędzy połówkami i scalamy
        count += mergeAndCount(pts, left, mid, right);
    }
    return count;
}


long long solve(vector<Point>& pts) {
    if (pts.empty()) return 0;


    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        if (a.x != b.x) {
            return a.x < b.x;
        }
        return a.y > b.y; 
    });


    return countPairsRecursive(pts, 0, pts.size() - 1);
}

int main() {

    vector<Point> P = {
        {1, 1},
        {2, 3},
        {3, 2},
        {4, 5},
        {5, 4},
        {1, 4}
    };

    cout << "Zbiór punktów:" << endl;
    for (const auto& p : P) {
        cout << "(" << p.x << ", " << p.y << ")" << endl;
    }

    long long result = solve(P);

    return 0;
}