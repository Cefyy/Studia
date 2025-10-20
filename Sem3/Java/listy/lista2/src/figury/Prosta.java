package figury;

public class Prosta {
    public final double a;
    public final double b;
    public final double c;


    public Prosta(double a,double b,double c)
    {
        this.a=a;
        this.b=b;
        this.c=c;
    }

    public static Prosta przesun_o_wektor(Wektor w1,Prosta p1)
    {
         double nowe_c = p1.c - p1.a * w1.dx - p1.b * w1.dy;
         return new Prosta(p1.a,p1.b,nowe_c);
    }

    public static boolean czyRownolegle(Prosta m,Prosta n)
    {
        return Math.abs(m.a*n.b-m.b*n.a) < 1e-10;
    }
    public static boolean czyProstopadle(Prosta m,Prosta n)
    {
        return Math.abs(m.a*n.a+m.b*n.b) < 1e-10;
    }
    public static Punkt przeciecie(Prosta m,Prosta n)
    {
        if(czyRownolegle(m,n))
        {
            throw new IllegalArgumentException("Proste są równoległe");
        }
        
        double W = m.a*n.b - m.b*n.a;

        double Wx = m.b*n.c - m.c*n.b;
        double Wy = m.c * n.a - m.a * n.c;
        
        double x = Wx/W;
        double y = Wy/W;
        return new Punkt(x,y);
    }
    
    @Override
    public String toString() {
        return "Prosta: " + a + "x + " + b + "y + " + c + " = 0";
    }

}
