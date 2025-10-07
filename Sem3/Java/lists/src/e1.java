//Zadanie 1
//Wprowadzic imie i rok urodzenia ze Scannera (Done)
//Wypisac w notacji rzymskiej (Done)
//Dopasowac patrona w kalendarzu chinskim
//Kodowanie polskich znaków


import java.util.Scanner;
class RokUrodzenia {
    private static final String[] rzymskie = {
            "M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I"
    };
    private static final int[] arabskie = {
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    };
    private static final String[] chinskie = {
            "Małpa","Kogut","Pies","Świnia","Szczur","Wół","Tygrys","Królik","Smok","Wąż","Koń","Owca",
    };
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rok;
        System.err.print("Podaj imie: ");
        String imie = sc.nextLine();
        while(true) {
            System.err.print("Wprowadz rok urodzenia: ");

            String rokUrodzenia = sc.nextLine();

            rok = Integer.parseInt(rokUrodzenia);

            if (rok < 0 || rok > 4000)
            {
                System.err.print("Rok musi znajdowac sie w przedziale 0 do 4000\n");
            }
            else
                break;
        }

        String rokRzymski = rzymska(rok);
        System.out.print("Imie: "+ imie + "Rok rzymski: " + rokRzymski);
    }
    public static String rzymska(int rok)
    {
        String roman="";
        int pt = 0;
        while(true)
        {

            if(rok >= arabskie[pt])
            {
                roman += rzymskie[pt];
                rok -= arabskie[pt];
            }
            else
            {
                pt++;
            }
            if(rok == 0)
            {
                break;
            }

        }
        return roman;
    }
    public static String[] chinskiZnak
}
