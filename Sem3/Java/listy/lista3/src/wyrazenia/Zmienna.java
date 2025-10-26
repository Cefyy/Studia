package wyrazenia;

public class Zmienna extends Wyrazenie {
    private final String nazwa;
    private static double wartosc = 0.0;

    public Zmienna(String nazwa) {
        this.nazwa = nazwa;
    }

    public static void ustaw(double nowa) {
        wartosc = nowa;
    }

    @Override
    public double oblicz() {
        return wartosc;
    }

    @Override
    public String toString() {
        return nazwa;
    }

    @Override
    protected int priorytet() { return 5; }

    @Override
    public boolean equals(Object o) {
        return (o instanceof Zmienna z) && this.nazwa.equals(z.nazwa);
    }
}
