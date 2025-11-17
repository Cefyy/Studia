package rozgrywka;

import obliczenia.Wymierna;

public class Gra {
    private int zakres;
    private Wymierna liczba;
    private int maksIloscProb;
    private int licznikProb;
    private StanGry stan;

    // Enum reprezentujący stany gry
    public enum StanGry {
        NIEAKTYWNA,
        AKTYWNA,
        REZYGNACJA,
        PORAZKA,
        ZWYCIESTWO
    }

    // Konstruktor
    public Gra() {
        this.stan = StanGry.NIEAKTYWNA;
        this.licznikProb = 0;
    }

    // Uruchomienie gry
    public void start(int z) {
        if (z < 5 || z > 20) {
            throw new IllegalArgumentException("Zakres musi być z przedziału [5, 20]");
        }
        
        zakres = z;
        
        // Losowanie licznika i mianownika
        int licz, mian;
        do {
            licz = (int) (Math.random() * zakres) + 1;
            mian = (int) (Math.random() * zakres) + 1;
        } while (licz >= mian);
        
        liczba = new Wymierna(licz, mian);
        
        // Inicjalizacja
        maksIloscProb = (int) Math.ceil(3 * Math.log(z) / Math.log(2));
        licznikProb = 0;
        stan = StanGry.AKTYWNA;
        
        // Asercja sprawdzająca czy 0 < liczba < 1
        assert liczba.getLicznik() > 0 && liczba.getLicznik() < liczba.getMianownik() 
            : "Wylosowana liczba nie spełnia warunku 0 < liczba < 1";
    }

    // Próba odgadnięcia liczby
    public String proba(Wymierna propozycja) {
        if (stan != StanGry.AKTYWNA) {
            throw new IllegalStateException("Gra nie jest aktywna");
        }

        licznikProb++;

        int porownanie = propozycja.compareTo(liczba);

        if (porownanie == 0) {
            stan = StanGry.ZWYCIESTWO;
            return "Zgadza się! Wygrałeś w " + licznikProb + " próbach!";
        } else if (licznikProb >= maksIloscProb) {
            stan = StanGry.PORAZKA;
            return "Porażka! Wyczerpano limit prób. Prawidłowa liczba to: " + liczba;
        } else if (porownanie < 0) {
            return "Za mało! Pozostało prób: " + (maksIloscProb - licznikProb);
        } else {
            return "Za dużo! Pozostało prób: " + (maksIloscProb - licznikProb);
        }
    }

    // Rezygnacja z gry
    public void poddajSie() {
        if (stan == StanGry.AKTYWNA) {
            stan = StanGry.REZYGNACJA;
        }
    }

    // Gettery
    public StanGry getStan() {
        return stan;
    }

    public int getZakres() {
        return zakres;
    }

    public int getLicznikProb() {
        return licznikProb;
    }

    public int getMaksIloscProb() {
        return maksIloscProb;
    }

    public Wymierna getLiczba() {
        if (stan == StanGry.AKTYWNA) {
            throw new IllegalStateException("Nie można ujawnić liczby podczas aktywnej gry");
        }
        return liczba;
    }

    // Metoda pomocnicza do wyświetlania informacji o grze
    public String info() {
        StringBuilder sb = new StringBuilder();
        sb.append("Stan gry: ").append(stan).append("\n");
        sb.append("Zakres: ").append(zakres).append("\n");
        sb.append("Maksymalna liczba prób: ").append(maksIloscProb).append("\n");
        sb.append("Wykonane próby: ").append(licznikProb).append("\n");
        
        if (stan != StanGry.AKTYWNA && stan != StanGry.NIEAKTYWNA) {
            sb.append("Wylosowana liczba: ").append(liczba).append("\n");
        }
        
        return sb.toString();
    }
}
