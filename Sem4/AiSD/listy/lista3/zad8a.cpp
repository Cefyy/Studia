#include <iostream>
#include <vector>

using namespace std;

long long inversions_count = 0; // Globalny licznik inwersji

void merge(vector<int> &arr, int left, int mid, int right)
{
    vector<int> temp;
    int i = left;    // Wskaźnik na lewą połówkę
    int j = mid + 1; // Wskaźnik na prawą połówkę

    // Scalanie dwóch posortowanych połówek
    while (i <= mid && j <= right)
    {
        if (arr[i] <= arr[j])
        {
            temp.push_back(arr[i]);
            i++;
        }
        else
        {
            // MAGIA INWERSJI: arr[i] > arr[j]
            // Skoro lewa połówka jest posortowana rosnąco, to jeśli arr[i]
            // jest większe od arr[j], to wszystkie elementy na prawo od i
            // (w lewej połówce) również są większe od arr[j]!
            temp.push_back(arr[j]);

            // Dodajemy do wyniku liczbę pozostałych elementów w lewej połówce
            inversions_count += (mid - i + 1);
            j++;
        }
    }

    // Przepisanie reszty elementów (jeśli jakieś zostały)
    while (i <= mid)
    {
        temp.push_back(arr[i]);
        i++;
    }
    while (j <= right)
    {
        temp.push_back(arr[j]);
        j++;
    }

    // Skopiowanie posortowanej części z powrotem do głównej tablicy
    for (int k = left; k <= right; k++)
    {
        arr[k] = temp[k - left];
    }
}

void merge_sort(vector<int> &arr, int left, int right)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}