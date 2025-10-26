package wyrazenia;

public class Exp extends Wyrazenie {
    private final Wyrazenie arg;

    public Exp(Wyrazenie arg) { this.arg = arg; }

    @Override
    public double oblicz() {
        return Math.exp(arg.oblicz());
    }

    @Override
    public String toString() {
        return "exp(" + arg + ")";
    }

    @Override
    protected int priorytet() { return 4; }

    @Override
    public boolean equals(Object o) {
        return (o instanceof Exp e) && arg.equals(e.arg);
    }
}