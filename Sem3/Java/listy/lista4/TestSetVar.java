public class TestSetVar {
    
    public static void main(String[] args) throws CloneNotSupportedException {
        ArraySetVar vars = new ArraySetVar(5);
        vars.set("x", 10.5);
        vars.set("y", 20.3);
        vars.set("z", 15.7);
        System.out.println("Dodane: " + vars);
        System.out.println("Rozmiar: " + vars.size());
        
        System.out.println("\nWyszukiwanie 'x': " + vars.search("x"));
        System.out.println("Pobranie 'x': " + vars.get("x"));
        
        vars.set("x", 25.5);
        System.out.println("\nPo aktualizacji 'x': " + vars);
        
        vars.del("y");
        System.out.println("Po usunięciu 'y': " + vars);
        
        ArraySetVar klon = vars.clone();
        klon.set("x", 100.0);
        System.out.println("\nOryginał: " + vars);
        System.out.println("Klon:     " + klon);
        
        vars.clear();
        System.out.println("\nPo clear(): " + vars);
        System.out.println("Rozmiar: " + vars.size());
    }
}
