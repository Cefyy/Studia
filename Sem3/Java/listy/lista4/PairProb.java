public class PairProb extends Pair {
    
    // Konstruktor dla prawdopodobieństwa
    public PairProb(String key, double probability) 
    {
        super(key, probability);
        // Walidacja zakresu (0, 1) w konstruktorze
        if (probability < 0.0 || probability > 1.0) {
            throw new IllegalArgumentException("Probability must be between 0.0 and 1.0, got: " + probability);
        }
    }
    
    // Nadpisanie metody set() aby walidować wartość
    @Override
    public void set(double probability) 
    {
        if (probability < 0.0 || probability > 1.0) {
            throw new IllegalArgumentException("Probability must be between 0.0 and 1.0, got: " + probability);
        }
        super.set(probability);
    }
}
