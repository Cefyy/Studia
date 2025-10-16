import figury.*;

public class TestFigur {
    public static void main(String[] args) {

        System.out.println("=== TEST KLASY WEKTOR ===");
        Wektor w1 = new Wektor(2, 3);
        Wektor w2 = new Wektor(-1, 5);
        Wektor w3 = Wektor.zlozWektory(w1, w2);
        System.out.println("Wektor 1: " + w1);
        System.out.println("Wektor 2: " + w2);
        System.out.println("Złożenie w1 + w2: " + w3);
        // Oczekiwany wynik: Wektor(1.0, 8.0)
        System.out.println();

        System.out.println("=== TEST KLASY PROSTA ===");
        Prosta p1 = new Prosta(1, -1, 0);   // y = x
        Prosta p2 = new Prosta(1, 1, -4);   // y = -x + 4
        Prosta p3 = Prosta.przesun_o_wektor(w1, p1);
        System.out.println("p1: " + p1);    // 1x - 1y + 0 = 0
        System.out.println("p2: " + p2);    // 1x + 1y - 4 = 0
        System.out.println("p1 przesunięta o w1: " + p3);
        // nowe C = 0 - 1*2 - (-1)*3 = 0 - 2 + 3 = 1 → oczekiwany: Prosta: 1x -1y +1 = 0
        System.out.println("Czy p1 i p2 są równoległe? " + Prosta.czyRownolegle(p1, p2)); // false
        System.out.println("Czy p1 i p2 są prostopadłe? " + Prosta.czyProstopadle(p1, p2)); // true
        Punkt przeciecie = Prosta.przeciecie(p1, p2);
        System.out.println("Punkt przecięcia p1 i p2: " + przeciecie);
        // Rozwiązanie układu:
        // y = x
        // y = -x + 4  →  x = 2, y = 2
        // Oczekiwany wynik: (2.0, 2.0)
        System.out.println();

        System.out.println("=== TEST KLASY PUNKT ===");
        Punkt A = new Punkt(1, 1);
        System.out.println("Punkt A: " + A);  // (1, 1)
        A.przesun(w1); // w1(2,3)
        System.out.println("A po przesunięciu o w1: " + A); 
        // (1+2, 1+3) → (3, 4)
        A.obroc(new Punkt(0,0), Math.PI/2);
        System.out.println("A po obrocie o 90° wokół (0,0): " + A);
        // (3,4) obrót o 90° → (-4,3)
        A.odbij(p1); 
        System.out.println("A po odbiciu względem prostej y=x: " + A);
        // odbicie (-4,3) względem y=x → (3,-4)
        System.out.println();

        System.out.println("=== TEST KLASY ODCINEK ===");
        Punkt B = new Punkt(0, 0);
        Punkt C = new Punkt(3, 0);
        Odcinek odc = new Odcinek(B, C);
        System.out.println("Odcinek przed przesunięciem: " + odc);
        odc.przesun(w2);
        System.out.println("Odcinek po przesunięciu o w2: " + odc);
        // przesunięcie o (-1,5): (0,0)->(-1,5), (3,0)->(2,5)
        odc.obroc(new Punkt(0, 0), Math.PI / 2);
        System.out.println("Odcinek po obrocie o 90° wokół (0,0): " + odc);
        // obrót o 90°: (-1,5)->(-5,-1), (2,5)->(-5,2)
        odc.odbij(p1);
        System.out.println("Odcinek po odbiciu względem prostej y=x: " + odc);
        // odbicie względem y=x: (-5,-1)->(-1,-5), (-5,2)->(2,-5)
        System.out.println();

        System.out.println("=== TEST KLASY TROJKAT ===");
        Punkt T1 = new Punkt(0, 0);
        Punkt T2 = new Punkt(3, 0);
        Punkt T3 = new Punkt(0, 4);
        Trojkat troj = new Trojkat(T1, T2, T3);
        System.out.println("Trójkąt przed przesunięciem: " + troj);
        troj.przesun(w1);
        System.out.println("Trójkąt po przesunięciu o w1: " + troj);
        // każdy punkt + (2,3): (2,3), (5,3), (2,7)
        troj.obroc(new Punkt(0, 0), Math.PI / 2);
        System.out.println("Trójkąt po obrocie o 90° wokół (0,0): " + troj);
        // (2,3)->(-3,2), (5,3)->(-3,5), (2,7)->(-7,2)
        troj.odbij(p1);
        System.out.println("Trójkąt po odbiciu względem y=x: " + troj);
        // odbicie względem y=x: (-3,2)->(2,-3), (-3,5)->(5,-3), (-7,2)->(2,-7)
    }
}
