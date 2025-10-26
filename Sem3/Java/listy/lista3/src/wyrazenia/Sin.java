package wyrazenia;

public class Sin extends Wyrazenie {
    private final Wyrazenie arg;
    public Sin(Wyrazenie arg) { this.arg = arg; }

    @Override public double oblicz() { return Math.sin(arg.oblicz()); }
    @Override public String toString() { return "sin(" + arg + ")"; }
    @Override protected int priorytet() { return 4; }
    @Override public boolean equals(Object o) { return (o instanceof Sin s) && arg.equals(s.arg); }
}
