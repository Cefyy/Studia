package obliczenia;

/**
 * Klasa reprezentująca liczbę wymierną w postaci nieskracalnego ułamka.
 * <p>
 * Liczba wymierna jest reprezentowana jako para liczb całkowitych: licznik i mianownik.
 * Ułamek jest automatycznie sprowadzany do postaci nieskracalnej, a znak minusa
 * jest zawsze przenoszony do licznika.
 * </p>
 * 
 * @author Jakub Grzelak
 * @version 1.0
 * @since 2025-11-17
 */
public class Wymierna implements Comparable<Wymierna> {
    /** Licznik ułamka */
    private int licznik;
    
    /** Mianownik ułamka (zawsze dodatni) */
    private int mianownik = 1;

    /**
     * Konstruktor bezparametrowy tworzący liczbę wymierną reprezentującą zero (0/1).
     */
    public Wymierna() {
        this(0, 1);
    }

    /**
     * Konstruktor jednoparametrowy tworzący liczbę całkowitą w postaci ułamka k/1.
     * Jest to konstruktor delegatowy wykorzystujący konstruktor dwuparametrowy.
     * 
     * @param k licznik ułamka (liczba całkowita)
     */
    public Wymierna(int k) {
        this(k, 1);
    }

    /**
     * Konstruktor dwuparametrowy tworzący liczbę wymierną k/m w postaci nieskracalnej.
     * <p>
     * Konstruktor wykonuje następujące operacje:
     * <ul>
     *   <li>Sprawdza czy mianownik jest różny od zera</li>
     *   <li>Przenosi znak minusa do licznika (mianownik zawsze dodatni)</li>
     *   <li>Skraca ułamek dzieląc licznik i mianownik przez ich NWD</li>
     * </ul>
     * </p>
     * 
     * @param k licznik ułamka
     * @param m mianownik ułamka
     * @throws IllegalArgumentException jeśli mianownik jest równy zero
     * 
     * @see #nwd(int, int)
     */
    public Wymierna(int k, int m) {
        if (m == 0) {
            throw new IllegalArgumentException("Mianownik nie może być zerem");
        }

        // Przeniesienie znaku do licznika
        if (m < 0) {
            k = -k;
            m = -m;
        }

        // Skracanie ułamka
        int nwd = nwd(Math.abs(k), m);
        this.licznik = k / nwd;
        this.mianownik = m / nwd;
    }

    /**
     * Oblicza największy wspólny dzielnik (NWD) dwóch liczb całkowitych
     * przy użyciu rekurencyjnego algorytmu Euklidesa.
     * 
     * @param a pierwsza liczba całkowita (nieujemna)
     * @param b druga liczba całkowita (nieujemna)
     * @return największy wspólny dzielnik liczb a i b
     */
    private int nwd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return nwd(b, a % b);
    }

    /**
     * Zwraca licznik ułamka.
     * 
     * @return licznik liczby wymiernej
     */
    public int getLicznik() {
        return licznik;
    }

    /**
     * Zwraca mianownik ułamka (zawsze dodatni).
     * 
     * @return mianownik liczby wymiernej
     */
    public int getMianownik() {
        return mianownik;
    }

    /**
     * Zwraca tekstową reprezentację liczby wymiernej.
     * <p>
     * Jeśli mianownik wynosi 1, zwracana jest tylko wartość licznika.
     * W przeciwnym przypadku zwracany jest format "licznik/mianownik".
     * </p>
     * 
     * @return reprezentacja tekstowa liczby wymiernej
     */
    @Override
    public String toString() {
        if (mianownik == 1) {
            return String.valueOf(licznik);
        }
        return licznik + "/" + mianownik;
    }

    /**
     * Porównuje tę liczbę wymierną z innym obiektem pod względem równości.
     * <p>
     * Dwie liczby wymierne są równe, gdy mają identyczne liczniki i mianowniki
     * (po sprowadzeniu do postaci nieskracalnej).
     * </p>
     * 
     * @param obj obiekt do porównania
     * @return true jeśli obiekty są równe, false w przeciwnym razie
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        
        Wymierna other = (Wymierna) obj;
        return licznik == other.licznik && mianownik == other.mianownik;
    }

    /**
     * Zwraca kod hash dla liczby wymiernej.
     * 
     * @return kod hash obliczony na podstawie licznika i mianownika
     */
    @Override
    public int hashCode() {
        return 31 * licznik + mianownik;
    }

    /**
     * Porównuje tę liczbę wymierną z inną liczbą wymierną.
     * <p>
     * Porównanie odbywa się poprzez mnożenie na krzyż:
     * a/b &lt; c/d wtedy i tylko wtedy gdy a*d &lt; b*c
     * </p>
     * 
     * @param other liczba wymierna do porównania
     * @return wartość ujemna jeśli this &lt; other, zero jeśli są równe,
     *         wartość dodatnia jeśli this &gt; other
     */
    @Override
    public int compareTo(Wymierna other) {
        // Porównujemy a/b z c/d poprzez a*d z b*c
        long left = (long) this.licznik * other.mianownik;
        long right = (long) other.licznik * this.mianownik;
        return Long.compare(left, right);
    }

    /**
     * Dodaje dwie liczby wymierne.
     * <p>
     * Wzór: a/b + c/d = (a*d + b*c) / (b*d)
     * </p>
     * 
     * @param w1 pierwsza liczba wymierna
     * @param w2 druga liczba wymierna
     * @return suma w1 + w2 w postaci nieskracalnej
     */
    public static Wymierna dodaj(Wymierna w1, Wymierna w2) {
        int nowyLicznik = w1.licznik * w2.mianownik + w2.licznik * w1.mianownik;
        int nowyMianownik = w1.mianownik * w2.mianownik;
        return new Wymierna(nowyLicznik, nowyMianownik);
    }

    /**
     * Odejmuje dwie liczby wymierne.
     * <p>
     * Wzór: a/b - c/d = (a*d - b*c) / (b*d)
     * </p>
     * 
     * @param w1 odjemna (liczba, od której odejmujemy)
     * @param w2 odjemnik (liczba, którą odejmujemy)
     * @return różnica w1 - w2 w postaci nieskracalnej
     */
    public static Wymierna odejmij(Wymierna w1, Wymierna w2) {
        int nowyLicznik = w1.licznik * w2.mianownik - w2.licznik * w1.mianownik;
        int nowyMianownik = w1.mianownik * w2.mianownik;
        return new Wymierna(nowyLicznik, nowyMianownik);
    }

    /**
     * Mnoży dwie liczby wymierne.
     * <p>
     * Wzór: a/b * c/d = (a*c) / (b*d)
     * </p>
     * 
     * @param w1 pierwsza liczba wymierna
     * @param w2 druga liczba wymierna
     * @return iloczyn w1 * w2 w postaci nieskracalnej
     */
    public static Wymierna pomnoz(Wymierna w1, Wymierna w2) {
        int nowyLicznik = w1.licznik * w2.licznik;
        int nowyMianownik = w1.mianownik * w2.mianownik;
        return new Wymierna(nowyLicznik, nowyMianownik);
    }

    /**
     * Dzieli dwie liczby wymierne.
     * <p>
     * Wzór: a/b / c/d = (a*d) / (b*c)
     * </p>
     * 
     * @param w1 dzielna (liczba dzielona)
     * @param w2 dzielnik (liczba przez którą dzielimy)
     * @return iloraz w1 / w2 w postaci nieskracalnej
     * @throws ArithmeticException jeśli w2 jest zerem
     */
    public static Wymierna podziel(Wymierna w1, Wymierna w2) {
        if (w2.licznik == 0) {
            throw new ArithmeticException("Dzielenie przez zero");
        }
        int nowyLicznik = w1.licznik * w2.mianownik;
        int nowyMianownik = w1.mianownik * w2.licznik;
        return new Wymierna(nowyLicznik, nowyMianownik);
    }
}
