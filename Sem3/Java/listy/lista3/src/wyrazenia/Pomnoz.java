package wyrazenia;

public class Pomnoz extends Wyrazenie {
    private final Wyrazenie lewy, prawy;

    public Pomnoz(Wyrazenie lewy, Wyrazenie prawy) {
        this.lewy = lewy;
        this.prawy = prawy;
    }

    @Override
    public double oblicz() {
        return lewy.oblicz() * prawy.oblicz();
    }

    @Override
    public String toString() {
        String s1 = (lewy.priorytet() < priorytet()) ? "(" + lewy + ")" : lewy.toString();
        String s2 = (prawy.priorytet() < priorytet()) ? "(" + prawy + ")" : prawy.toString();
        return s1 + " * " + s2;
    }

    @Override
    protected int priorytet() { return 2; }

    @Override
    public boolean equals(Object o) {
        return (o instanceof Pomnoz m) && lewy.equals(m.lewy) && prawy.equals(m.prawy);
    }
}
