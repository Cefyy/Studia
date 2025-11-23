import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;


public class Powierzchnia extends Canvas {
    
    

    private ArrayList<Kreska> drawing;
    private Point tempStart;
    private Point nowPoint;
    private Color currColor;
    private boolean isDrawing;


    public Powierzchnia() {
        drawing = new ArrayList<>();
        currColor=Color.BLACK;
        isDrawing = false;
        setBackground(Color.WHITE);
        

        addMouseListener(new MouseAdapter()
        {
            @Override
            public void mousePressed(MouseEvent e)
            {
                tempStart = e.getPoint();
                nowPoint = e.getPoint();
                isDrawing = true;
            }
            @Override
            public void mouseReleased(MouseEvent e)
            {
                if(isDrawing)
                {
                    Point end = e.getPoint();
                    if(end.x >=0 && end.x <= getWidth() && end.y >= 0 && end.y <= getHeight())
                    {
                        drawing.add(new Kreska(tempStart,end,currColor));
                    }
                    isDrawing=false;
                    repaint();
                }
            }
        });
        
        addMouseMotionListener(new MouseMotionAdapter()
            {
                @Override
                public void mouseDragged(MouseEvent e)
                {
                    if(isDrawing)
                    {
                        nowPoint = e.getPoint();
                        repaint();
                    }
                }
            }
        );

    }
    

    @Override
    public void paint(Graphics gr)
    {
        for(Kreska k: drawing)
        {
            gr.setColor(k.getColor());
            gr.drawLine(k.getStart().x,k.getStart().y,k.getEnd().x,k.getEnd().y);
        }
        if(isDrawing && tempStart != null && nowPoint != null)
        {
            gr.setColor(Color.LIGHT_GRAY);
            gr.drawLine(tempStart.x,tempStart.y,nowPoint.x,nowPoint.y);
        }
    }
    


    public void setColor(Color color)
    {
        this.currColor=color;
    }


    public void clearAll()
    {
        drawing.clear();
        repaint();
    }

    public void deleteFirst()
    {
        if(!drawing.isEmpty())
        {
            drawing.remove(0);
            repaint();
        }
    }
    
    public void deleteLast()
    {
        if(!drawing.isEmpty())
        {
            drawing.remove(drawing.size()-1);
            repaint();
        }
    }
}
