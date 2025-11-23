import java.awt.Color;
import java.awt.Point;


public class Kreska {
    protected Point start,end;
    protected Color color;
    

    public Kreska(Point start, Point end, Color color) {
       this.start=start;
       this.end=end;
       this.color=color;
    }
    

    public Point getStart() {
        return start;
    }

    public Point getEnd()
    {
        return end;
    }

    public Color getColor()
    {
        return color;
    }
}
