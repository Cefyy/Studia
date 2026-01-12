package hellofx;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.scene.layout.HBox;
import javafx.scene.input.KeyCode;

public class Controller {

    @FXML
    private Label titleLabel;
    
    @FXML
    private VBox container;
    
    private TextField[] fields;
    private String[] previousValues;
    private static final String[] BASE_NAMES = {
        "Binarny (2)", "Trójkowy (3)", "Czwórkowy (4)", "Piątkowy (5)",
        "Szóstkowy (6)", "Siódemkowy (7)", "Ósemkowy (8)", "Dziewiątkowy (9)",
        "Dziesiętny (10)", "Jedenastkowy (11)", "Dwunastkowy (12)", "Trzynastkowy (13)",
        "Czternastkowy (14)", "Piętnastkowy (15)", "Szesnastkowy (16)"
    };

    public void initialize() {
        fields = new TextField[15];
        previousValues = new String[15];
        
        for (int i = 0; i < 15; i++) {
            previousValues[i] = "";
        }
        
        
        for (int i = 0; i < 15; i++) {
            final int base = i + 2;
            final int index = i;
            
            HBox row = new HBox();
            row.getStyleClass().add("row");
            
            
            if (base == 10) {
                row.getStyleClass().add("decimal-row");
            }
            
            Label baseLabel = new Label(BASE_NAMES[i]);
            baseLabel.getStyleClass().add("base-label");
            
            TextField field = new TextField();
            field.setPromptText("Wartość w systemie " + base);
            field.getStyleClass().add("number-field");
            
            fields[index] = field;
            
            
            field.textProperty().addListener((obs, oldVal, newVal) -> {
                if (!isValidForBase(newVal, base)) {
                    field.setText(oldVal);
                }
            });
            

            field.setOnKeyPressed(event -> {
                if (event.getCode() == KeyCode.ENTER) {
                    String input = field.getText().trim();
                    if (!input.isEmpty()) {
                        convertFromBase(base, index);
                        previousValues[index] = input;
                    }
                }
            });
            
            field.focusedProperty().addListener((obs, wasFocused, isNowFocused) -> {
                if (wasFocused && !isNowFocused) {
                    String currentValue = field.getText().trim();
                    if (!currentValue.equals(previousValues[index])) {

                        field.setText(previousValues[index]);
                    }
                }
            });
            
            row.getChildren().addAll(baseLabel, field);
            container.getChildren().add(row);
        }
    }
    
    private boolean isValidForBase(String text, int base) {
        if (text == null || text.isEmpty()) {
            return true;
        }
        

        String validChars;
        if (base <= 10) {
            validChars = "0123456789".substring(0, base);
        } else {
            validChars = "0123456789ABCDEF".substring(0, base);
        }
        

        for (char c : text.toUpperCase().toCharArray()) {
            if (validChars.indexOf(c) == -1) {
                return false;
            }
        }
        return true;
    }
    
    private void convertFromBase(int sourceBase, int sourceIndex) {
        String input = fields[sourceIndex].getText().trim().toUpperCase();
        if (input.isEmpty()) return;
        
        try {
            
            long decimal = Long.parseLong(input, sourceBase);
            
            
            for (int i = 0; i < 15; i++) {
                int targetBase = i + 2;
                String converted = Long.toString(decimal, targetBase).toUpperCase();
                fields[i].setText(converted);
                previousValues[i] = converted;
            }
        } catch (NumberFormatException e) {
            
            System.err.println("Błąd konwersji dla systemu " + sourceBase + ": " + input);
            fields[sourceIndex].setText(previousValues[sourceIndex]);
        }
    }
}