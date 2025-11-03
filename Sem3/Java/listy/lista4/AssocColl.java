public interface AssocColl { 
    void set(String k, double v); 
    double get(String k); 
    boolean search(String k); 
    String[] names(); 
    
    // Metoda domyślna - reprezentacja tekstowa zbioru zmiennych
    default String defaultToString() {
        String[] keys = names();
        if (keys == null || keys.length == 0) {
            return "[]";
        }
        
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < keys.length; i++) {
            sb.append(keys[i]).append("=").append(get(keys[i]));
            if (i < keys.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }
}

