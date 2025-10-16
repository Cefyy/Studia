package figury;

public class Wektor {
    final public double dx;
    final public double dy;


    public Wektor(double dx,double dy)
    {
        this.dx = dx;
        this.dy = dy;
    }

    public static Wektor zlozWektory(Wektor w1,Wektor w2)
    {
        return new Wektor(w1.dx+w2.dx,w1.dy+w2.dy);
    }
    
    @Override
    public String toString() {
        return "Wektor(" + dx + ", " + dy + ")";
    }
}
