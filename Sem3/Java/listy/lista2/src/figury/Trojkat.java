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

    public void przesun(Wektor w)
    {
        this.p1.przesun(w);
        this.p2.przesun(w);
        this.p3.przesun(w);
    }
    public void obroc(Punkt p, double kat)
    {
        p1.obroc(p, kat);
        p2.obroc(p, kat);
        p3.obroc(p, kat);
    }
    public void odbij(Prosta p)
    {
        p1.odbij(p);
        p2.odbij(p);
        p3.odbij(p);
    }

    private boolean saWspoliniowe(Punkt p1,Punkt p2,Punkt p3)
    {
        double wyznacznik = (p2.getX() - p1.getX()) * (p3.getY() - p1.getY())
                          - (p2.getY() - p1.getY()) * (p3.getX() - p1.getX());

        return (Math.abs(wyznacznik) < 1e-10);
    }
    
    @Override
    public String toString() {
        return "Trojkat[" + p1 + ", " + p2 + ", " + p3 + "]";
    }

}
