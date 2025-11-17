package rozgrywka.wyjatki;

public class BlednaLiczbaWymiernaException extends Exception {
    public BlednaLiczbaWymiernaException(String message) {
        super(message);
    }
    
    public BlednaLiczbaWymiernaException(String message, Throwable cause) {
        super(message, cause);
    }
}
