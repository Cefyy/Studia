package figury;

public class Trojkat {
    private Punkt p1;
    private Punkt p2;
    private Punkt p3;


    public Trojkat(Punkt p1,Punkt p2,Punkt p3)
    {
        if(p1.eq(p2) || p2.eq(p3) || p3.eq(p1))
        {
            throw new IllegalArgumentException("Punkty nie są różne");
        }
        if(saWspoliniowe(p1, p2, p3))
        {
            throw new IllegalArgumentException("Punkty są współliniowe");
        }
        
        this.p1=p1;
        this.p2=p2;
        this.p3=p3;
    }



    private boolean saWspoliniowe(Punkt p1,Punkt p2,Punkt p3)
    {
        double wyznacznik = (p2.getX() - p1.getX()) * (p3.getY() - p1.getY())
                          - (p2.getY() - p1.getY()) * (p3.getX() - p1.getX());

        return (Math.abs(wyznacznik) < 1e-10);
    }
}
