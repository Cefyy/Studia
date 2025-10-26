package wyrazenia;

public abstract class Wyrazenie implements Obliczalny {

    public static double suma(Wyrazenie... wyr) {
        double s = 0;
        for (Wyrazenie w : wyr)
            s += w.oblicz();
        return s;
    }

    public static double iloczyn(Wyrazenie... wyr) {
        double p = 1;
        for (Wyrazenie w : wyr)
            p *= w.oblicz();
        return p;
    }

    /** priorytet operatora lub funkcji */
    protected abstract int priorytet();

    @Override
    public abstract String toString();

    @Override
    public abstract boolean equals(Object o);
}
