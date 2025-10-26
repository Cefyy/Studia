package wyrazenia;


public class Potega extends Wyrazenie {
    private final Wyrazenie podstawa;
    private final Wyrazenie wykladnik;

    public Potega(Wyrazenie podstawa, Wyrazenie wykladnik) {
        this.podstawa = podstawa;
        this.wykladnik = wykladnik;
    }

    @Override
    public double oblicz() {
        return Math.pow(podstawa.oblicz(), wykladnik.oblicz());
    }

    @Override
    public String toString() {

        String s1 = (podstawa.priorytet() < priorytet()) ? "(" + podstawa + ")" : podstawa.toString();
        String s2 = (wykladnik.priorytet() <= priorytet()) ? "(" + wykladnik + ")" : wykladnik.toString();
        return s1 + " ^ " + s2;
    }

    @Override
    protected int priorytet() { 

        return 3; 
    }

    @Override
    public boolean equals(Object o) {
        return (o instanceof Potega p)
            && podstawa.equals(p.podstawa)
            && wykladnik.equals(p.wykladnik);
    }
}