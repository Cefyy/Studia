import java.io.Serializable;

public class SolitaireModel implements Serializable {
    private static final long serialVersionUID = 1L;

    public enum BoardType { BRITISH, EUROPEAN }
    

    private int[][] board;
    private BoardType currentType = BoardType.BRITISH;
    private boolean gameInProgress = false; 
    

    private int selectedX = -1;
    private int selectedY = -1;

    private int cursorX = 3;
    private int cursorY = 3;

    public SolitaireModel() {
        resetGame();
    }

    public void setBoardType(BoardType type) {
        this.currentType = type;
        resetGame();
    }

    public BoardType getBoardType() { return currentType; }

    public void resetGame() {
        board = new int[7][7];
        

        for (int y = 0; y < 7; y++) {
            for (int x = 0; x < 7; x++) {
                if ((x < 2 || x > 4) && (y < 2 || y > 4)) {
                    board[y][x] = 0;
                } else {
                    board[y][x] = 1;
                }
            }
        }
        
        board[3][3] = 2;

        if (currentType == BoardType.EUROPEAN) {
            board[1][1] = 1; board[1][5] = 1;
            board[5][1] = 1; board[5][5] = 1;
        }

        selectedX = -1;
        selectedY = -1;
        cursorX = 3;
        cursorY = 3;
        gameInProgress = false;
    }

    public int getCell(int x, int y) {
        if (x < 0 || x >= 7 || y < 0 || y >= 7) return 0;
        return board[y][x];
    }

    public int getCursorX() { return cursorX; }
    public int getCursorY() { return cursorY; }

    public void moveCursor(int dx, int dy) {
        int newX = cursorX + dx;
        int newY = cursorY + dy;

        if (newX >= 0 && newX < 7 && newY >= 0 && newY < 7 && board[newY][newX] != 0) {
            cursorX = newX;
            cursorY = newY;
        }
    }


    public void activateCell(int x, int y) {
        int cell = getCell(x, y);
        
        if (cell == 1) {

            if (selectedX == x && selectedY == y) {
                selectedX = -1;
                selectedY = -1;
            } else {
                selectedX = x;
                selectedY = y;
            }
        } else if (cell == 2 && selectedX != -1) {
            if (tryMove(selectedX, selectedY, x, y)) {
                selectedX = -1;
                selectedY = -1;
                gameInProgress = true;
            }
        }
    }

    public boolean attemptJump(int dx, int dy) {
        if (selectedX == -1) return false;
        int targetX = selectedX + (dx * 2);
        int targetY = selectedY + (dy * 2);
        
        if (tryMove(selectedX, selectedY, targetX, targetY)) {
            selectedX = -1;
            selectedY = -1;
            gameInProgress = true;
            return true;
        }
        return false;
    }

    public boolean isSelected(int x, int y) {
        return x == selectedX && y == selectedY;
    }

    private boolean tryMove(int x1, int y1, int x2, int y2) {
        if (x2 < 0 || x2 >= 7 || y2 < 0 || y2 >= 7) return false;
        if (board[y2][x2] != 2) return false; 

        if (Math.abs(x1 - x2) == 2 && y1 == y2) {
            int midX = (x1 + x2) / 2;
            if (board[y1][midX] == 1) { 
                makeMove(x1, y1, midX, y1, x2, y2);
                return true;
            }
        } else if (Math.abs(y1 - y2) == 2 && x1 == x2) {
            int midY = (y1 + y2) / 2;
            if (board[midY][x1] == 1) {
                makeMove(x1, y1, x1, midY, x2, y2);
                return true;
            }
        }
        return false;
    }

    private void makeMove(int fromX, int fromY, int midX, int midY, int toX, int toY) {
        board[fromY][fromX] = 2; 
        board[midY][midX] = 2;   
        board[toY][toX] = 1;     

        cursorX = toX;
        cursorY = toY;
    }

    public boolean isGameOver() {
        if (getPegCount() == 1 && board[3][3] == 1) return true;
        return !hasPossibleMoves();
    }

    public boolean hasWon() {
        return getPegCount() == 1 && board[3][3] == 1;
    }

    public int getPegCount() {
        int count = 0;
        for (int[] row : board) for (int cell : row) if (cell == 1) count++;
        return count;
    }
    
    public boolean isGameInProgress() {
        return gameInProgress && !isGameOver();
    }

    public String getGameStateMessage() {
        if (!gameInProgress) return "Rozpocznij grę";
        return "Pionów na planszy: " + getPegCount();
    }

    private boolean hasPossibleMoves() {
        for (int y = 0; y < 7; y++) {
            for (int x = 0; x < 7; x++) {
                if (board[y][x] == 1) {
                    if (canJump(x, y, 2, 0)) return true;
                    if (canJump(x, y, -2, 0)) return true;
                    if (canJump(x, y, 0, 2)) return true;
                    if (canJump(x, y, 0, -2)) return true;
                }
            }
        }
        return false;
    }

    private boolean canJump(int x, int y, int dx, int dy) {
        int tx = x + dx;
        int ty = y + dy;
        int mx = x + dx/2;
        int my = y + dy/2;
        if (tx < 0 || tx >= 7 || ty < 0 || ty >= 7) return false;
        return board[ty][tx] == 2 && board[my][mx] == 1;
    }
}