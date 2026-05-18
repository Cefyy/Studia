int opt[N][N]; // Nowa tablica do trzymania optymalnych miejsc cięć

int solve()
{
    // 1. Inicjalizacja bazowa (rozpiętość 1)
    for (int i = 0; i < n + 1; i++)
    {
        dp[i][i + 1] = 0;
        opt[i][i + 1] = i + 1; // Inicjujemy optymalne cięcie (formalność dla przedziałów dł. 1)
    }

    // 2. Główna pętla po rozpiętości (k to Twoje j - i)
    for (int k = 2; k < n + 2; k++)
    {
        for (int i = 0, j = i + k; j < n + 2; j++, i++)
        {

            int result = 2e9; // Używamy większej stałej "nieskończoności"
            int best_z = -1;

            // 3. MAGIA KNUTHA - zawężone granice pętli!
            // Zamiast: for (int z = i + 1; z < j; z++)
            // Robimy to:
            for (int z = opt[i][j - 1]; z <= opt[i + 1][j]; z++)
            {

                // Upewniamy się, że z nie wyjdzie poza logiczne granice cięcia (i, j)
                if (z > i && z < j)
                {
                    int cost = dp[i][z] + dp[z][j] + (A[j] - A[i]);
                    if (cost < result)
                    {
                        result = cost;
                        best_z = z; // Zapamiętujemy, gdzie było najtaniej
                    }
                }
            }
            dp[i][j] = result;
            opt[i][j] = best_z; // Zapisujemy optymalny punkt dla potomności
        }
    }
    return dp[0][n + 1];
}