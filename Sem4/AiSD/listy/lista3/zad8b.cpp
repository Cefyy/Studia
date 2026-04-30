#include <iostream>
#include <vector>

using namespace std;

// Struktura do trzymania wartości razem z jej oryginalnym indeksem
struct Element
{
    int value;
    int original_index;
};

const int MAX_N = 100005;
long long L_greater[MAX_N]; // Ile większych elementów stało po lewej
long long R_smaller[MAX_N]; // Ile mniejszych elementów stało po prawej

void merge_triplets(vector<Element> &arr, int left, int mid, int right)
{
    vector<Element> temp;
    int i = left;
    int j = mid + 1;

    // Zmienna 'j_start' to kopia początkowej pozycji wskaźnika prawej połówki.
    // Używamy jej do obliczania, ile elementów z prawej strony już wzięliśmy.
    int j_start = mid + 1;

    while (i <= mid && j <= right)
    {
        if (arr[i].value <= arr[j].value)
        {
            // Zdejmujemy z LEWEJ połówki
            // Oznacza to, że arr[i] "przeskoczyło" przez elementy z prawej
            // połówki, które wzięliśmy do tej pory.
            // Liczba wziętych elementów to dokładnie (j - j_start).
            int elements_taken_from_right = j - j_start;
            R_smaller[arr[i].original_index] += elements_taken_from_right;

            temp.push_back(arr[i]);
            i++;
        }
        else
        {
            // Zdejmujemy z PRAWEJ połówki (arr[j].value < arr[i].value)
            // Oznacza to, że wszystkie elementy, które ZOSTAŁY w lewej połówce,
            // są od arr[j] większe i stały oryginalnie po jego lewej stronie.
            int remaining_in_left = mid - i + 1;
            L_greater[arr[j].original_index] += remaining_in_left;

            temp.push_back(arr[j]);
            j++;
        }
    }

    // Przepisanie reszty elementów z LEWEJ strony
    // (One też muszą wiedzieć, ile elementów z prawej je przeskoczyło)
    while (i <= mid)
    {
        int elements_taken_from_right = j - j_start;
        R_smaller[arr[i].original_index] += elements_taken_from_right;
        temp.push_back(arr[i]);
        i++;
    }

    // Przepisanie reszty elementów z PRAWEJ strony
    // (Skoro bierzemy z prawej, a lewa jest pusta, to nikt więcej z lewej nie jest większy)
    while (j <= right)
    {
        temp.push_back(arr[j]);
        j++;
    }

    for (int k = left; k <= right; k++)
    {
        arr[k] = temp[k - left];
    }
}

void merge_sort_triplets(vector<Element> &arr, int left, int right)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;
        merge_sort_triplets(arr, left, mid);
        merge_sort_triplets(arr, mid + 1, right);
        merge_triplets(arr, left, mid, right);
    }
}

// === GŁÓWNA FUNKCJA ROZWIĄZUJĄCA ZADANIE ===
long long count_decreasing_triplets(vector<int> &input_array)
{
    int n = input_array.size();
    vector<Element> arr(n);

    // Inicjalizacja tablicy par (wartość, indeks)
    for (int i = 0; i < n; ++i)
    {
        arr[i].value = input_array[i];
        arr[i].original_index = i;
        L_greater[i] = 0;
        R_smaller[i] = 0;
    }

    // Odpalamy naszego zmodyfikowanego Merge Sorta
    merge_sort_triplets(arr, 0, n - 1);

    // Na koniec zliczamy wynik z reguły mnożenia dla każdego elementu
    long long total_triplets = 0;
    for (int i = 0; i < n; ++i)
    {
        total_triplets += (L_greater[i] * R_smaller[i]);
    }

    return total_triplets;
}