package wyrazenia;

public class Odwrotnosc extends Wyrazenie {
    private final Wyrazenie arg;

    public Odwrotnosc(Wyrazenie arg) {
        this.arg = arg;
    }

    @Override
    public double oblicz() {
        double v = arg.oblicz();
        if (v == 0)
            throw new ArithmeticException("Dzielenie przez zero w odwrotności: " + this);
        return 1.0 / v;
    }

    @Override
    public String toString() {
        String s = (arg.priorytet() > priorytet()) ? arg.toString() : "(" + arg + ")";
        return "!" + s;
    }

    @Override
    protected int priorytet() { return 3; }

    @Override
    public boolean equals(Object o) {
        return (o instanceof Odwrotnosc od) && arg.equals(od.arg);
    }
}
