import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SolitairePanel extends JPanel {
    private SolitaireModel model;
    private SolitaireGame controller;
    
    private Color boardColor = new Color(222, 184, 135);
    private Color pegColor = new Color(0, 0, 139);
    private boolean filledPegs = true; 

    public SolitairePanel(SolitaireModel model, SolitaireGame controller) {
        this.model = model;
        this.controller = controller;
        setFocusable(true); 
        
        // Obsługa Myszki
        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                requestFocusInWindow(); 
                if (model.isGameOver()) return;

                int size = Math.min(getWidth(), getHeight());
                int cellSize = size / 7;
                int offsetX = (getWidth() - size) / 2;
                int offsetY = (getHeight() - size) / 2;

                int col = (e.getX() - offsetX) / cellSize;
                int row = (e.getY() - offsetY) / cellSize;

                if (col >= 0 && col < 7 && row >= 0 && row < 7) {

                    if (model.getCell(col, row) != 0) {
                        model.moveCursor(col - model.getCursorX(), row - model.getCursorY());
                        model.activateCell(col, row);
                        controller.checkGameState();
                        repaint();
                    }
                }
            }
        });

        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (model.isGameOver()) return;
                
                switch (e.getKeyCode()) {
                    case KeyEvent.VK_UP:    model.moveCursor(0, -1); break;
                    case KeyEvent.VK_DOWN:  model.moveCursor(0, 1); break;
                    case KeyEvent.VK_LEFT:  model.moveCursor(-1, 0); break;
                    case KeyEvent.VK_RIGHT: model.moveCursor(1, 0); break;
                    case KeyEvent.VK_SPACE: 
                    case KeyEvent.VK_ENTER:
                        model.activateCell(model.getCursorX(), model.getCursorY());
                        controller.checkGameState();
                        break;
                }
                repaint();
            }
        });
    }

    public void setBoardColor(Color c) { this.boardColor = c; repaint(); }
    public Color getBoardColor() { return boardColor; }
    public void setPegColor(Color c) { this.pegColor = c; repaint(); }
    public Color getPegColor() { return pegColor; }
    public void setFilledPegs(boolean f) { this.filledPegs = f; repaint(); }
    public boolean isFilledPegs() { return filledPegs; }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        int size = Math.min(getWidth(), getHeight());
        int cellSize = size / 7;
        int offsetX = (getWidth() - size) / 2;
        int offsetY = (getHeight() - size) / 2;
        int boardDiameter = cellSize * 7;

        g2.setColor(boardColor);
        g2.fillOval(offsetX, offsetY, boardDiameter, boardDiameter);

        for (int y = 0; y < 7; y++) {
            for (int x = 0; x < 7; x++) {
                int cellType = model.getCell(x, y);
                if (cellType == 0) continue;

                int cx = offsetX + x * cellSize;
                int cy = offsetY + y * cellSize;
                int padding = cellSize / 6;
                int ovalSize = cellSize - 2 * padding;


                g2.setColor(new Color(0, 0, 0, 50));
                g2.fillOval(cx + padding, cy + padding, ovalSize, ovalSize);


                if (cellType == 1) {
                    g2.setColor(pegColor);
                    if (filledPegs) {
                        g2.fillOval(cx + padding, cy + padding, ovalSize, ovalSize);
                        g2.setColor(new Color(255, 255, 255, 100));
                    } else {
                        g2.setStroke(new BasicStroke(3));
                        g2.drawOval(cx + padding, cy + padding, ovalSize, ovalSize);
                    }
                }


                if (model.isSelected(x, y)) {
                    g2.setColor(Color.RED);
                    g2.setStroke(new BasicStroke(3));
                    g2.drawOval(cx + padding - 2, cy + padding - 2, ovalSize + 4, ovalSize + 4);
                }

                if (x == model.getCursorX() && y == model.getCursorY()) {
                    g2.setColor(Color.YELLOW);
                    g2.setStroke(new BasicStroke(2));
                    g2.drawRect(cx, cy, cellSize, cellSize);
                }
            }
        }
    }
}