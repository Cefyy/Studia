package wyrazenia;

public class Odejmij extends Wyrazenie {
    private final Wyrazenie lewy, prawy;

    public Odejmij(Wyrazenie lewy, Wyrazenie prawy) {
        this.lewy = lewy;
        this.prawy = prawy;
    }

    @Override
    public double oblicz() {
        return lewy.oblicz() - prawy.oblicz();
    }

    @Override
    public String toString() {
        String s1 = (lewy.priorytet() < priorytet()) ? "(" + lewy + ")" : lewy.toString();
        String s2 = (prawy.priorytet() <= priorytet()) ? "(" + prawy + ")" : prawy.toString();
        return s1 + " - " + s2;
    }

    @Override
    protected int priorytet() { return 1; }

    @Override
    public boolean equals(Object o) {
        return (o instanceof Odejmij d) && lewy.equals(d.lewy) && prawy.equals(d.prawy);
    }
}
