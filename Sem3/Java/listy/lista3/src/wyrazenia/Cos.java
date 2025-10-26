package wyrazenia;

public class Cos extends Wyrazenie {
    private final Wyrazenie arg;
    public Cos(Wyrazenie arg) { this.arg = arg; }

    @Override public double oblicz() { return Math.cos(arg.oblicz()); }
    @Override public String toString() { return "Cos(" + arg + ")"; }
    @Override protected int priorytet() { return 4; }
    @Override public boolean equals(Object o) { return (o instanceof Cos c) && arg.equals(c.arg); }
}
