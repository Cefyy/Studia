package rozgrywka.wyjatki;

public class NieprawidlowyFormatException extends BlednaLiczbaWymiernaException {
    public NieprawidlowyFormatException(String message) {
        super(message);
    }
    
    public NieprawidlowyFormatException(String message, Throwable cause) {
        super(message, cause);
    }
}
