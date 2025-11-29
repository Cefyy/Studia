import structures.SimpleList;
import java.util.Date;

public class TestSimpleList {
    
    public static void main(String[] args) {
        System.out.println("=== TEST SIMPLELIST<INTEGER> ===\n");
        testInteger();
        
        System.out.println("\n=== TEST SIMPLELIST<STRING> ===\n");
        testString();
        
        System.out.println("\n=== TEST SIMPLELIST<DATE> ===\n");
        testDate();
        
        System.out.println("\n=== TEST ITERATOR ===\n");
        testIterator();
        
        System.out.println("\n=== TEST WYJATKOW ===\n");
        testExceptions();
    }
    
    private static void testInteger() {
        SimpleList<Integer> list = new SimpleList<>();
        
        System.out.println("Pusta lista: " + list.empty());
        System.out.println("Rozmiar: " + list.size());
        
        list.insert(5, 0);
        list.insert(10, 1);
        list.insert(3, 0);
        list.insert(7, 2);
        System.out.println("Po dodaniu [3, 5, 7, 10]: " + list);
        System.out.println("Rozmiar: " + list.size());
        
        System.out.println("Min: " + list.min());
        System.out.println("Max: " + list.max());
        
        System.out.println("Element na pozycji 2: " + list.at(2));
        System.out.println("Pozycja elementu 7: " + list.index(7));
        
        System.out.println("Czy jest 5? " + list.search(5));
        System.out.println("Czy jest 100? " + list.search(100));
        
        list.remove(Integer.valueOf(5));
        System.out.println("Po usunieciu 5: " + list);
        
        list.remove(0);
        System.out.println("Po usunieciu pozycji 0: " + list);
        
        System.out.println("For-each:");
        for (Integer val : list) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
    
    private static void testString() {
        SimpleList<String> list = new SimpleList<>();
        
        list.insert("banana", 0);
        list.insert("apple", 0);
        list.insert("cherry", 2);
        list.insert("date", 3);
        System.out.println("Lista stringow: " + list);
        
        System.out.println("Min: " + list.min());
        System.out.println("Max: " + list.max());
        
        System.out.println("Pozycja 'cherry': " + list.index("cherry"));
        System.out.println("Czy jest 'banana'? " + list.search("banana"));
        
        list.remove("apple");
        System.out.println("Po usunieciu 'apple': " + list);
        
        System.out.println("For-each:");
        for (String s : list) {
            System.out.print(s + " ");
        }
        System.out.println();
    }
    
    private static void testDate() {
        SimpleList<Date> list = new SimpleList<>();
        
        Date now = new Date();
        Date past = new Date(now.getTime() - 86400000);
        Date future = new Date(now.getTime() + 86400000);
        
        list.insert(now, 0);
        list.insert(past, 0);
        list.insert(future, 2);
        
        System.out.println("Lista dat (3 elementy)");
        System.out.println("Rozmiar: " + list.size());
        System.out.println("Min (najstarsza): " + list.min());
        System.out.println("Max (najnowsza): " + list.max());
        
        System.out.println("For-each:");
        for (Date d : list) {
            System.out.println("  " + d);
        }
    }
    
    private static void testIterator() {
        SimpleList<Integer> list = new SimpleList<>();
        list.insert(1, 0);
        list.insert(2, 1);
        list.insert(3, 2);
        
        System.out.println("Lista: " + list);
        System.out.println("Iteracja for-each:");
        for (Integer val : list) {
            System.out.print(val + " ");
        }
        System.out.println();
        
        System.out.println("\nTest modyfikacji podczas iteracji:");
        try {
            for (Integer val : list) {
                System.out.print(val + " ");
                if (val == 2) {
                    list.insert(99, 0);
                }
            }
        } catch (IllegalStateException e) {
            System.out.println("\nZlapano IllegalStateException: " + e.getMessage());
        }
    }
    
    private static void testExceptions() {
        SimpleList<Integer> list = new SimpleList<>();
        
        try {
            System.out.println("Proba wstawienia null:");
            list.insert(null, 0);
        } catch (NullPointerException e) {
            System.out.println("Zlapano NullPointerException: " + e.getMessage());
        }
        
        try {
            System.out.println("\nProba pobrania z pustej listy:");
            list.at(0);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Zlapano IndexOutOfBoundsException: " + e.getMessage());
        }
        
        try {
            System.out.println("\nProba min() na pustej liscie:");
            list.min();
        } catch (Exception e) {
            System.out.println("Zlapano wyjątek: " + e.getMessage());
        }
        
        list.insert(5, 0);
        try {
            System.out.println("\nProba wstawienia na zla pozycje:");
            list.insert(10, 10);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Zlapano IndexOutOfBoundsException: " + e.getMessage());
        }
        
        try {
            System.out.println("\nProba usuniecia z zlej pozycji:");
            list.remove(10);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Zlapano IndexOutOfBoundsException: " + e.getMessage());
        }
    }
}
