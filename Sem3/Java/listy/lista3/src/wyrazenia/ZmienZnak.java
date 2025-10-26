package wyrazenia;

public class ZmienZnak extends Wyrazenie {
    private final Wyrazenie arg;

    public ZmienZnak(Wyrazenie arg) {
        this.arg = arg;
    }

    @Override
    public double oblicz() {
        return -arg.oblicz();
    }

    @Override
    public String toString() {
        String s = (arg.priorytet() > priorytet()) ? arg.toString() : "(" + arg + ")";
        return "~" + s;
    }

    @Override
    protected int priorytet() { return 3; }

    @Override
    public boolean equals(Object o) {
        return (o instanceof ZmienZnak z) && arg.equals(z.arg);
    }
}
