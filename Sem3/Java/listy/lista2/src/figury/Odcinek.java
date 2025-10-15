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

    


}
