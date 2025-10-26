package wyrazenia;

public class Stala extends Wyrazenie {
    private final String nazwa;
    private final double wartosc;

    public static final Stala PI = new Stala("pi", Math.PI);
    public static final Stala E = new Stala("e", Math.E);

    public Stala(String nazwa, double wartosc) {
        this.nazwa = nazwa;
        this.wartosc = wartosc;
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
        return (o instanceof Stala s) && this.nazwa.equals(s.nazwa);
    }
}
