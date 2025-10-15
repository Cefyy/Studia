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

    public boolean eq(Punkt p)
    {
        return this == p || Math.abs(this.x-p.x) < 1e-10 && Math.abs(this.y-p.y) < 1e-10;
    }
}

