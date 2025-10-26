package wyrazenia;


public class Logarytm extends Wyrazenie {
    private final Wyrazenie podstawa;
    private final Wyrazenie argument;

    public Logarytm(Wyrazenie podstawa, Wyrazenie argument) {
        this.podstawa = podstawa;
        this.argument = argument;
    }

    @Override
    public double oblicz() {
        double a = argument.oblicz();
        double b = podstawa.oblicz();

        if (a <= 0 || b <= 0 || b == 1)
            throw new ArithmeticException("Niepoprawne wartości w logarytmie: log(" + b + ", " + a + ")");

        return Math.log(a) / Math.log(b);
    }

    @Override
    public String toString() {
        return "log(" + podstawa + ", " + argument + ")";
    }

    @Override
    protected int priorytet() { 

        return 4; 
    }

    @Override
    public boolean equals(Object o) {
        return (o instanceof Logarytm l)
            && podstawa.equals(l.podstawa)
            && argument.equals(l.argument);
    }
}