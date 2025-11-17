import rozgrywka.Gra;
import rozgrywka.Gra.StanGry;
import rozgrywka.wyjatki.*;
import obliczenia.Wymierna;
import java.util.Scanner;
import java.util.logging.*;
import java.io.*;

/**
 * Glowna klasa programu - gra logiczna "Zgadywanka".
 * <p>
 * Aplikacja losuje liczbe wymierna z przedzialu (0, 1) a gracz
 * probuje ja odgadnać w ograniczonej liczbie prob.
 * </p>
 * 
 * @author Kuba
 * @version 1.0
 */
public class Zgadywanka {
    private static final Logger logger = Logger.getLogger("rozgrywka");

    public static void main(String[] args) {
        // Konfiguracja loggera
        try {
            LogManager.getLogManager().readConfiguration(
                new FileInputStream("logging.properties")
            );
            logger.info("=== URUCHOMIENIE APLIKACJI GRY ===");
        } catch (IOException e) {
            System.err.println("Nie mozna zaladować pliku konfiguracyjnego logging.properties");
            e.printStackTrace();
        }

        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== GRA: ODGADNIJ LICZBE WYMIERNA ===\n");
        System.out.print("Podaj Imie ");
        String imieGracza = scanner.nextLine();
        logger.info("Gracz: " + imieGracza);
        
        boolean graWToku = true;
        
        while (graWToku) {
            Gra gra = new Gra();
            int zakres = 0;
            

            while (zakres == 0) {
                System.out.print("Podaj zakres (5-20): ");
                try {
                    zakres = Integer.parseInt(scanner.nextLine());
                } catch (NumberFormatException e) {
                    System.out.println("Blad: Podaj liczbe calkowita!");
                    logger.warning("Nieprawidlowy format zakresu: " + e.getMessage());
                }
            }

            try {
                long startCzas = System.currentTimeMillis();
                gra.start(zakres);
                logger.info("Rozpoczecie nowej rundy - zakres: " + zakres + 
                           ", max prob: " + gra.getMaksIloscProb());
                
                System.out.println("Gra rozpoczeta!");
                System.out.println("Maksymalna liczba prob: " + gra.getMaksIloscProb());
                System.out.println("Odgadnij liczbe wymierna z przedzialu (0, 1)");
                System.out.println("Format: licznik mianownik (np. 1 2 dla 1/2)\n");

                while (gra.getStan() == StanGry.AKTYWNA) {
                    System.out.print("Proba " + (gra.getLicznikProb() + 1) + ": ");
                    String wejscie = scanner.nextLine();
                    
                    try {
                        Wymierna propozycja = parsujLiczbeWymierna(wejscie, zakres);
                        logger.info("Gracz " + imieGracza + " podal: " + propozycja);
                        
                        String wynik = gra.proba(propozycja);
                        System.out.println(wynik);
                        logger.info("Wynik proby: " + wynik);
                        System.out.println();
                        
                    } catch (BlednaLiczbaWymiernaException e) {
                        System.out.println("BLAD: " + e.getMessage());
                        logger.warning("Blad wprowadzania danych: " + e.getMessage());
                        System.out.println();
                    }
                }

                long koniecCzas = System.currentTimeMillis();
                long czasTrwania = (koniecCzas - startCzas) / 1000;
                
                System.out.println("\n=== KONIEC RUNDY ===");
                System.out.println("Czas trwania: " + czasTrwania + " sekund");
                
                String wynik = "";
                if (gra.getStan() == StanGry.ZWYCIESTWO) {
                    wynik = imieGracza + " WYGRAL!";
                    System.out.println(wynik);
                } else if (gra.getStan() == StanGry.PORAZKA) {
                    wynik = "PORAZKA";
                    System.out.println(wynik);
                    System.out.println("Prawidlowa odpowiedź: " + gra.getLiczba());
                }
                
                logger.info("Koniec rundy - " + wynik + " - Czas: " + czasTrwania + "s - " +
                           "Proby: " + gra.getLicznikProb() + "/" + gra.getMaksIloscProb());

            } catch (IllegalArgumentException e) {
                System.out.println("Blad: " + e.getMessage());
                logger.severe("Blad parametrow gry: " + e.getMessage());
            } catch (AssertionError e) {
                System.out.println("Asercja nieudana: Wylosowano liczbe >= 1");
                System.out.println("Sprobuj ponownie z wlaczonymi asercjami (-ea)");
                logger.severe("Asercja nieudana: " + e.getMessage());
            }
            
            System.out.print("\nCzy chcesz zagrać ponownie? (t/n): ");
            String odpowiedz = scanner.nextLine().toLowerCase();
            graWToku = odpowiedz.equals("t") || odpowiedz.equals("tak");
            
            if (graWToku) {
                logger.info("Gracz " + imieGracza + " rozpoczyna nowa runde");
                System.out.println();
            }
        }
        logger.info("Gracz " + imieGracza + " zakonczyl gre");
        logger.info("=== ZAMKNIeCIE APLIKACJI ===");
        
        scanner.close();
    }
    
    /**
     * Parsuje wejście uzytkownika i tworzy liczbe wymierna z walidacja.
     * <p>
     * Metoda sprawdza:
     * <ul>
     *   <li>Poprawność formatu (dwie liczby oddzielone spacja)</li>
     *   <li>Czy mozna przekonwertować na liczby calkowite</li>
     *   <li>Czy mianownik nie przekracza zakresu</li>
     *   <li>Czy liczba nalezy do przedzialu (0, 1)</li>
     * </ul>
     * </p>
     * 
     * @param wejscie tekst wprowadzony przez uzytkownika
     * @param zakres maksymalny dozwolony mianownik
     * @return utworzona liczba wymierna
     * @throws BlednaLiczbaWymiernaException jeśli dane sa nieprawidlowe
     */
    private static Wymierna parsujLiczbeWymierna(String wejscie, int zakres) 
            throws BlednaLiczbaWymiernaException {
        
        String[] czesci = wejscie.trim().split("\\s+");
        
        if (czesci.length != 2) {
            throw new NieprawidlowyFormatException(
                "Podaj dokladnie dwie liczby oddzielone spacja (licznik mianownik)");
        }
        
        int licznik, mianownik;
        
        try {
            licznik = Integer.parseInt(czesci[0]);
            mianownik = Integer.parseInt(czesci[1]);
        } catch (NumberFormatException e) {
            throw new NieprawidlowyFormatException(
                "Nie mozna przekonwertować na liczby calkowite", e);
        }
        
        // Sprawdzenie mianownika
        if (mianownik > zakres) {
            throw new MianownikZaduzyException(
                "Mianownik (" + mianownik + ") przekracza maksymalny zakres (" + zakres + ")");
        }
        
        // Utworzenie liczby wymiernej
        Wymierna w;
        try {
            w = new Wymierna(licznik, mianownik);
        } catch (IllegalArgumentException e) {
            throw new NieprawidlowyFormatException(
                "Nieprawidlowa liczba wymierna: " + e.getMessage(), e);
        }
        
        // Sprawdzenie czy w przedziale (0, 1)
        Wymierna zero = new Wymierna(0, 1);
        Wymierna jeden = new Wymierna(1, 1);
        
        if (w.compareTo(zero) <= 0 || w.compareTo(jeden) >= 0) {
            throw new LiczbaSpozaZakresuException(
                "Liczba " + w + " jest poza przedzialem (0, 1)");
        }
        
        return w;
    }
}
