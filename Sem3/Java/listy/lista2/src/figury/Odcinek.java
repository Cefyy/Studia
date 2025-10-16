package figury;

public class Odcinek {
    private Punkt p1;
    private Punkt p2;

    public Odcinek(Punkt p1,Punkt p2)
    {
        if(p1.eq(p2))
        {
            throw new IllegalArgumentException("Punkty nie są różne");
        }
        this.p1 = p1;
        this.p2 = p2;
    }

    public void przesun(Wektor w)
    {
        this.p1.przesun(w);
        this.p2.przesun(w);
    }
    public void obroc(Punkt p, double kat)
    {
        p1.obroc(p, kat);
        p2.obroc(p, kat);
    }
    public void odbij(Prosta p)
    {
        p1.odbij(p);
        p2.odbij(p);
    }
    
    @Override
    public String toString() {
        return "Odcinek[" + p1 + " -> " + p2 + "]";
    }

}
