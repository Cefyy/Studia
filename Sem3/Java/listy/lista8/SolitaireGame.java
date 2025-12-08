import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class SolitaireGame extends JFrame {

    private SolitaireModel model;
    private SolitairePanel boardPanel;
    private JLabel statusLabel;
    
    private JRadioButtonMenuItem rbBritish;
    private JRadioButtonMenuItem rbEuropean;

    public SolitaireGame() {
        super("Samotnik - Peg Solitaire");
        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        setSize(600, 650);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        File saveFile = new File("solitaire.ser");
        if (saveFile.exists()) {
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(saveFile))) {
                model = (SolitaireModel) ois.readObject();
                saveFile.delete();
            } catch (Exception e) {
                model = new SolitaireModel();
            }
        } else {
            model = new SolitaireModel();
        }


        statusLabel = new JLabel("Stan gry: " + model.getGameStateMessage(), SwingConstants.CENTER);
        statusLabel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        add(statusLabel, BorderLayout.SOUTH);


        boardPanel = new SolitairePanel(model, this);
        add(boardPanel, BorderLayout.CENTER);


        createMenuBar();


        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                if (model.isGameInProgress()) {
                    try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("solitaire.ser"))) {
                        oos.writeObject(model);
                    } catch (IOException ex) {
                        ex.printStackTrace();
                    }
                }
                System.exit(0);
            }
        });

        updateSettingsAvailability();
        setVisible(true);
        boardPanel.requestFocusInWindow();
    }

    private void createMenuBar() {
        JMenuBar menuBar = new JMenuBar();

        JMenu menuGame = new JMenu("Gra");
        menuGame.setMnemonic(KeyEvent.VK_G);

        JMenuItem itemNew = new JMenuItem("Nowa", KeyEvent.VK_N);
        itemNew.addActionListener(e -> startNewGame());
        
        JMenuItem itemExit = new JMenuItem("Koniec", KeyEvent.VK_K);
        itemExit.addActionListener(e -> dispatchEvent(new WindowEvent(this, WindowEvent.WINDOW_CLOSING)));

        menuGame.add(itemNew);
        menuGame.addSeparator();
        menuGame.add(itemExit);


        JMenu menuMoves = new JMenu("Ruchy");
        addMoveMenuItem(menuMoves, "Skok w górę", KeyEvent.VK_UP, 0, -1);
        addMoveMenuItem(menuMoves, "Skok w dół", KeyEvent.VK_DOWN, 0, 1);
        addMoveMenuItem(menuMoves, "Skok w lewo", KeyEvent.VK_LEFT, -1, 0);
        addMoveMenuItem(menuMoves, "Skok w prawo", KeyEvent.VK_RIGHT, 1, 0);

        JMenu menuSettings = new JMenu("Ustawienia");

        ButtonGroup bgGroup = new ButtonGroup();
        rbBritish = new JRadioButtonMenuItem("Plansza Brytyjska");
        rbEuropean = new JRadioButtonMenuItem("Plansza Europejska");
        
        rbBritish.setSelected(model.getBoardType() == SolitaireModel.BoardType.BRITISH);
        rbEuropean.setSelected(model.getBoardType() == SolitaireModel.BoardType.EUROPEAN);

        ActionListener typeListener = e -> {
            if (rbBritish.isSelected()) model.setBoardType(SolitaireModel.BoardType.BRITISH);
            else model.setBoardType(SolitaireModel.BoardType.EUROPEAN);
            boardPanel.repaint();
            boardPanel.requestFocusInWindow();
        };
        rbBritish.addActionListener(typeListener);
        rbEuropean.addActionListener(typeListener);

        bgGroup.add(rbBritish);
        bgGroup.add(rbEuropean);
        menuSettings.add(rbBritish);
        menuSettings.add(rbEuropean);
        menuSettings.addSeparator();


        JMenuItem colorBoardItem = new JMenuItem("Kolor planszy...");
        colorBoardItem.addActionListener(e -> {
            Color c = JColorChooser.showDialog(this, "Wybierz kolor planszy", boardPanel.getBoardColor());
            if (c != null) boardPanel.setBoardColor(c);
        });
        menuSettings.add(colorBoardItem);

        JMenuItem colorPegItem = new JMenuItem("Kolor pionów...");
        colorPegItem.addActionListener(e -> {
            Color c = JColorChooser.showDialog(this, "Wybierz kolor pionów", boardPanel.getPegColor());
            if (c != null) boardPanel.setPegColor(c);
        });
        menuSettings.add(colorPegItem);


        JCheckBoxMenuItem filledPegsItem = new JCheckBoxMenuItem("Wypełnij piony");
        filledPegsItem.setSelected(boardPanel.isFilledPegs());
        filledPegsItem.addActionListener(e -> boardPanel.setFilledPegs(filledPegsItem.isSelected()));
        menuSettings.add(filledPegsItem);

        JMenu menuHelp = new JMenu("Pomoc");
        
        JMenuItem itemAboutGame = new JMenuItem("O grze");
        itemAboutGame.addActionListener(e -> JOptionPane.showMessageDialog(this, 
            "Zasady gry Samotnik:\n1. Poruszaj się strzałkami lub myszką.\n2. Spacja/Enter lub kliknięcie zaznacza piona.\n3. Przeskocz innego piona, aby go zbić.", 
            "O grze", JOptionPane.INFORMATION_MESSAGE));

        JMenuItem itemAboutApp = new JMenuItem("O aplikacji");
        itemAboutApp.addActionListener(e -> JOptionPane.showMessageDialog(this, 
            "Samotnik v1.0\n", 
            "O aplikacji", JOptionPane.INFORMATION_MESSAGE));
        menuHelp.add(itemAboutGame);
        menuHelp.add(itemAboutApp);
        menuBar.add(menuGame);
        menuBar.add(menuMoves);
        menuBar.add(menuSettings);
        menuBar.add(Box.createHorizontalGlue());
        menuBar.add(menuHelp);

        setJMenuBar(menuBar);
    }

    private void addMoveMenuItem(JMenu menu, String label, int key, int dx, int dy) {
        JMenuItem item = new JMenuItem(label);
        item.setAccelerator(KeyStroke.getKeyStroke(key, InputEvent.CTRL_DOWN_MASK));
        item.addActionListener(e -> {
            if (model.attemptJump(dx, dy)) {
                checkGameState();
                boardPanel.repaint();
            }
        });
        menu.add(item);
    }

    public void startNewGame() {
        model.resetGame();
        checkGameState(); 
        updateSettingsAvailability();
        boardPanel.repaint();
        boardPanel.requestFocusInWindow();
    }

    public void checkGameState() {
        statusLabel.setText("Stan gry: " + model.getGameStateMessage());
        
        if (model.isGameOver()) {
            String msg = model.hasWon() ? "Zwycięstwo! Jeden pion na środku." : "Przegrana. Zostało pionów: " + model.getPegCount();
            statusLabel.setText(msg);
            updateSettingsAvailability();
        }
    }

    private void updateSettingsAvailability() {
        boolean canChangeSettings = !model.isGameInProgress();
        rbBritish.setEnabled(canChangeSettings);
        rbEuropean.setEnabled(canChangeSettings);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SolitaireGame::new);
    }
}