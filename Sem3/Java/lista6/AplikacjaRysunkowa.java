import java.awt.*;
import java.awt.event.*;



public class AplikacjaRysunkowa extends Frame
{
    private Powierzchnia canvas;
    private CheckboxGroup radioColors;


    private static final Color[] Colors=
    {
        Color.BLACK, Color.RED, Color.BLUE, Color.GREEN, 
        Color.YELLOW, Color.ORANGE, Color.PINK, Color.MAGENTA
    };
    private static final String[] Color_Names=
    {
        "Black", "Red", "Blue", "Green",
        "Yellow", "Orange", "Pink", "Magenta"
    };

    public AplikacjaRysunkowa()
    {
        super("Aplikacja Rysunkowa");

        setSize(1024,768);
        setLayout(new BorderLayout(10,10));

        canvas = new Powierzchnia();
        canvas.setFocusable(true);

        add(canvas, BorderLayout.CENTER);



        radioColors = new CheckboxGroup();
        Panel radioClrsPanel = new Panel();

        radioClrsPanel.setLayout(new GridLayout(Colors.length+1,1));
        for(int i=0;i< Color_Names.length;i++)
        {
            final int indeks = i;
            Checkbox radio = new Checkbox(Color_Names[i],radioColors,indeks==0);
            radio.addItemListener(new ItemListener()
                {
                    @Override
                    public void itemStateChanged(ItemEvent e)
                    {
                        if(e.getStateChange() == ItemEvent.SELECTED)
                        {
                            canvas.setColor(Colors[indeks]);
                        }
                    }
                }
            );
            radioClrsPanel.add(radio);
        }
        add(radioClrsPanel,BorderLayout.EAST);


        canvas.addKeyListener(new KeyAdapter()
        {
            @Override
            public void keyPressed(KeyEvent e)
            {
                int code = e.getKeyCode();
                char key = e.getKeyChar();

                if(code == KeyEvent.VK_BACK_SPACE)
                {
                    canvas.clearAll();
                }
                else if(key == 'F' || key == 'f')
                {
                    canvas.deleteFirst();
                }
                else if(key == 'B' || key == 'b' || key == 'L' || key == 'l')
                {
                    canvas.deleteLast();
                }
            }
        });

        addWindowListener(new WindowAdapter()
        {
            @Override
            public void windowClosing(WindowEvent e)
            {
                dispose();
                System.exit(0);
            }
        });

        setVisible(true);
        canvas.requestFocus();

    }
    public static void main(String[] args)
    {
        new AplikacjaRysunkowa();
    }
}

