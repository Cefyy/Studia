package wyrazenia;

public class Podziel extends Wyrazenie {
    private final Wyrazenie lewy, prawy;

    public Podziel(Wyrazenie lewy, Wyrazenie prawy) {
        this.lewy = lewy;
        this.prawy = prawy;
    }

    @Override
    public double oblicz() {
        double dzielnik = prawy.oblicz();
        if (dzielnik == 0)
            throw new ArithmeticException("Dzielenie przez zero: " + this);
        return lewy.oblicz() / dzielnik;
    }

    @Override
    public String toString() {
        String s1 = (lewy.priorytet() < priorytet()) ? "(" + lewy + ")" : lewy.toString();
        String s2 = (prawy.priorytet() <= priorytet()) ? "(" + prawy + ")" : prawy.toString();
        return s1 + " / " + s2;
    }

    @Override
    protected int priorytet() { return 2; }

    @Override
    public boolean equals(Object o) {
        return (o instanceof Podziel d) && lewy.equals(d.lewy) && prawy.equals(d.prawy);
    }
}
