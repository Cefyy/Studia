/**
 * Pakiet zawierający klasy do operacji na liczbach wymiernych.
 * <p>
 * Główną klasą pakietu jest {@link obliczenia.Wymierna}, która reprezentuje
 * liczby wymierne w postaci nieskracalnych ułamków zwykłych.
 * </p>
 * 
 * <h2>Funkcjonalność pakietu:</h2>
 * <ul>
 *   <li>Reprezentacja liczb wymiernych jako ułamków w postaci nieskracalnej</li>
 *   <li>Automatyczne skracanie ułamków przy użyciu algorytmu Euklidesa</li>
 *   <li>Podstawowe operacje arytmetyczne: dodawanie, odejmowanie, mnożenie, dzielenie</li>
 *   <li>Porównywanie liczb wymiernych</li>
 *   <li>Konwersja do reprezentacji tekstowej</li>
 * </ul>
 * 
 * <h2>Przykład użycia:</h2>
 * <pre>{@code
 * // Tworzenie liczb wymiernych
 * Wymierna w1 = new Wymierna(3, 4);      // 3/4
 * Wymierna w2 = new Wymierna(1, 2);      // 1/2
 * 
 * // Operacje arytmetyczne
 * Wymierna suma = Wymierna.dodaj(w1, w2);           // 5/4
 * Wymierna roznica = Wymierna.odejmij(w1, w2);      // 1/4
 * Wymierna iloczyn = Wymierna.pomnoz(w1, w2);       // 3/8
 * Wymierna iloraz = Wymierna.podziel(w1, w2);       // 3/2
 * 
 * // Porównywanie
 * if (w1.compareTo(w2) > 0) {
 *     System.out.println(w1 + " jest większe od " + w2);
 * }
 * }</pre>
 */
package obliczenia;
