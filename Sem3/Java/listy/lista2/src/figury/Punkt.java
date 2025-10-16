package figury;

public class Punkt
{
    private double x;
    private double y;

    public Punkt(double x,double y)
    {
        this.x = x;
        this.y = y;
    }

    public double getX() {return x;}
    public double getY() {return y;}

    public void przesun(Wektor v) {
        this.x += v.dx;
        this.y += v.dy;
    }
    public void odbij(Prosta p) {
    double a = p.a;
    double b = p.b;
    double c = p.c;

    double d = a * a + b * b; // mianownik

    double newX = ((b * b - a * a) * x - 2 * a * b * y - 2 * a * c) / d;
    double newY = ((a * a - b * b) * y - 2 * a * b * x - 2 * b * c) / d;

    this.x = newX;
    this.y = newY;
    }

    public void obroc(Punkt srodek, double kat) {
        double dx = x - srodek.x;
        double dy = y - srodek.y;

        double newX = srodek.x + dx * Math.cos(kat) - dy * Math.sin(kat);
        double newY = srodek.y + dx * Math.sin(kat) + dy * Math.cos(kat);
        this.x = newX;
        this.y = newY;
    }

    public boolean eq(Punkt p)
    {
        return this == p || Math.abs(this.x-p.x) < 1e-10 && Math.abs(this.y-p.y) < 1e-10;
    }
    
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

