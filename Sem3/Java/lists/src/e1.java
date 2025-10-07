//Zadanie 1
//Wprowadzic imie i rok urodzenia ze Scannera (Done)
//Wypisac w notacji rzymskiej (Done)
//Dopasowac patrona w kalendarzu chinskim(Done)
//Kodowanie polskich znaków (Done)


import java.util.Scanner;
class RokUrodzenia {
    private static final String[] rzymskie = {
            "M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I"
    };
    private static final int[] arabskie = {
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    };
    private static final String[] chinskie = {
            "Szczur","Wół","Tygrys","Królik","Smok","Wąż","Koń","Owca","Małpa","Kogut","Pies","Świnia"
    };
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rok;
        System.err.print("Podaj imię: ");
        String imie = sc.nextLine();
        while(true) {
            System.err.print("Wprowadź rok urodzenia: ");

            String rokUrodzenia = sc.nextLine();

            rok = Integer.parseInt(rokUrodzenia);

            if (rok < 0 || rok > 4000)
            {
                System.err.print("Rok musi znajdować sie w przedziale 0 do 4000\n");
            }
            else
                break;
        }

        String rokRzymski = rzymska(rok);
        String chinskiZnakZodiaku=chinskiZnak(rok);
        System.out.print("Imię: "+ imie + "\n" + "Rok rzymski: " + rokRzymski + "\n" + "Chiński znak zodiaku: " + chinskiZnakZodiaku);
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
    public static String chinskiZnak(int rok)
    {
        return chinskie[(rok-4)%12];
    }
}
