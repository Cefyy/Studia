import numpy as np
import math

def efficient_romberg(f, a, b, max_m=20):

    # Inicjalizacja tablicy (wymiar 21x21, bo m od 0 do 20)
    T = np.zeros((max_m + 1, max_m + 1))
    

    h = b - a
    T[0, 0] = 0.5 * h * (f(a) + f(b))
    
    # Główna pętla po wierszach (m)
    for m in range(1, max_m + 1):
        # 1. Obliczamy sumę w nowych punktach (środki starych przedziałów)

        
        n_prev = 2**(m-1) # liczba podprzedziałów w poprzednim kroku
        h_current = (b - a) / (2**m) # aktualny krok h_m
        
        # Generujemy tylko nowe punkty: a + (2i - 1) * h_current
        # Używamy wektoryzacji numpy dla szybkości
        indices = np.arange(1, n_prev + 1)
        x_new = a + (2 * indices - 1) * h_current
        sum_f = np.sum(f(x_new))
        
        # 2. Rekurencyjny wzór trapezów: T_{2n} = 0.5 * T_n + h_current * sum_f

        T[m, 0] = 0.5 * T[m-1, 0] + h_current * sum_f
        
        # 3. Ekstrapolacja Richardsona (kolumny k)

        for k in range(1, m + 1):
            factor = 4**k
            T[m, k] = (factor * T[m, k-1] - T[m-1, k-1]) / (factor - 1)
            
    return T



# Funkcja A: Wielomian
def f1(x):
    return 2026*x**8 + 1977*x**6 - 1410*x**3 - 1791*x + 1

def exact_f1():
    # Całka nieoznaczona: 2026*x^9/9 + 1977*x^7/7 - 1410*x^4/4 - 1791*x^2/2 + x
    def F(x):
        return (2026/9)*x**9 + (1977/7)*x**7 - (1410/4)*x**4 - (1791/2)*x**2 + x
    return F(7) - F(-1)

# Funkcja B: 1 / (1 + 25x^2)
def f2(x):
    return 1.0 / (1.0 + 25.0 * x**2)

def exact_f2():
    # Całka z 1/(1+(5x)^2) dx to (1/5) * arctan(5x)
    return 0.2 * (math.atan(5*1) - math.atan(5*(-1)))

# Funkcja C: ln(x+1)
def f3(x):
    return np.log(x + 1)

def exact_f3():
    # Całka z ln(x+1) to (x+1)ln(x+1) - x
    val_b = (5+1)*math.log(5+1) - 5
    val_a = (0+1)*math.log(0+1) - 0
    return val_b - val_a


tasks = [
    ("A) Wielomian", f1, -1, 7, exact_f1()),
    ("B) 1/(1+25x^2)", f2, -1, 1, exact_f2()),
    ("C) ln(x+1)", f3, 0, 5, exact_f3())
]

print(f"{'Zadanie':<20} | {'Typ wyniku':<15} | {'Wartość całki':<20} | {'Błąd bezwzględny':<20}")
print("-" * 85)

for name, func, a, b, exact_val in tasks:
    # Obliczenie tablicy Romberga
    R = efficient_romberg(func, a, b, max_m=20)
    

    
    val_trapez = R[20, 0]
    val_best_constrained = R[10, 10]
    
    # Obliczamy błędy
    err_trapez = abs(val_trapez - exact_val)
    err_best = abs(val_best_constrained - exact_val)
    
    print(f"{name:<20} | {'Dokładna':<15} | {exact_val:.14e} | {'---':<20}")
    print(f"{'':<20} | {'T_20,0 (Trapez)':<15} | {val_trapez:.14e} | {err_trapez:.4e}")
    print(f"{'':<20} | {'T_10,10 (Romberg)':<15} | {val_best_constrained:.14e} | {err_best:.4e}")
    
    # Dla wielomianu (A) sprawdzamy czy T_4,4 jest już dokładne
    if "Wielomian" in name:
        val_poly = R[4, 4] 
        err_poly = abs(val_poly - exact_val)
        print(f"{'':<20} | {'T_4,4 (Teoria)':<15} | {val_poly:.14e} | {err_poly:.4e}")
        
    print("-" * 85)