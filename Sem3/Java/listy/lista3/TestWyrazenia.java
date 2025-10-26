import wyrazenia.*;

public class TestWyrazenia {
    public static void main(String[] args) {
        Zmienna.ustaw(1.618);
        Wyrazenie x = new Zmienna("x");

        Wyrazenie[] testy = new Wyrazenie[] {
            // 7 + 5 * x - 1
            new Odejmij(
                new Dodaj(new Liczba(7), new Pomnoz(new Liczba(5), x)),
                new Liczba(1)
            ),

            // ~ (2 - x) * e
            new Pomnoz(
                new ZmienZnak(new Odejmij(new Liczba(2), x)),
                Stala.E
            ),

            // (3 * π - 1) / (!x + 5)
            new Podziel(
                new Odejmij(new Pomnoz(new Liczba(3), Stala.PI), new Liczba(1)),
                new Dodaj(new Odwrotnosc(x), new Liczba(5))
            ),

            // sin((x + 13) * π / (1 - x))
            new Sin(
                new Podziel(
                    new Pomnoz(new Dodaj(x, new Liczba(13)), Stala.PI),
                    new Odejmij(new Liczba(1), x)
                )
            ),

            // exp(5) + x * log(e, x)
            new Dodaj(
                new Exp(new Liczba(5)),
                new Pomnoz(x, new Logarytm(Stala.E, x))
            )
        };

        for (Wyrazenie w : testy) {
            System.out.println(w);
            System.out.println("= " + w.oblicz());
            System.out.println();
        }
    }
}
