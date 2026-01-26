import numpy as np
import math

# --- 1. Silnik Romberga ---
def efficient_romberg(f, a, b, max_m=20):
    T = np.zeros((max_m + 1, max_m + 1))
    h = b - a
    T[0, 0] = 0.5 * h * (f(a) + f(b))
    
    for m in range(1, max_m + 1):
        n_prev = 2**(m-1)
        h_current = (b - a) / (2**m)
        indices = np.arange(1, n_prev + 1)
        x_new = a + (2 * indices - 1) * h_current
        sum_f = np.sum(f(x_new))
        
        T[m, 0] = 0.5 * T[m-1, 0] + h_current * sum_f
        
        for k in range(1, m + 1):
            factor = 4**k
            T[m, k] = (factor * T[m, k-1] - T[m-1, k-1]) / (factor - 1)
    return T

# --- 2. Definicje Funkcji ---
def f1(x): return 2026*x**8 + 1977*x**6 - 1410*x**3 - 1791*x + 1
def exact_f1(): 
    return (2026/9)*7**9 + (1977/7)*7**7 - (1410/4)*7**4 - (1791/2)*7**2 + 7 - \
           ((2026/9)*(-1)**9 + (1977/7)*(-1)**7 - (1410/4)*(-1)**4 - (1791/2)*(-1)**2 + (-1))

def f2(x): return 1.0 / (1.0 + 25.0 * x**2)
def exact_f2(): return 0.2 * (math.atan(5) - math.atan(-5))

def f3(x): return np.log(x + 1)
def exact_f3(): return (6*math.log(6) - 5) - (1*math.log(1) - 0)

# --- 3. Funkcja pokazująca przekątną z wartością dokładną ---
def show_diagonal_path(name, func, a, b, exact_val):
    print(f"\n{'#'*90}")
    print(f"ANALIZA DLA: {name}")
    print(f"DOKŁADNA WARTOŚĆ CAŁKI: {exact_val:.16f}") # Wyświetlamy z dużą precyzją
    print(f"{'#'*90}")
    
    # Nagłówek tabeli
    print(f"{'Elem.':<8} | {'Przybliżenie':<20} | {'Błąd bezwzględny':<20} | {'Poprawa rzędu (EOC)'}")
    print("-" * 90)
    
    R = efficient_romberg(func, a, b, max_m=10)
    
    prev_error = None
    
    # Idziemy po przekątnej: T[0,0] -> T[1,1] -> ... -> T[10,10]
    for i in range(11):
        val = R[i, i]
        error = abs(val - exact_val)
        
        # Obliczanie o ile razy zmalał błąd
        if prev_error is not None and error > 0 and prev_error > 0:
            ratio = prev_error / error
            improvement = f"{ratio:.1f}x" 
        elif error == 0:
            improvement = "Dokładny"
        else:
            improvement = "---"
            
        prev_error = error
        label = f"T[{i},{i}]"
        
        print(f"{label:<8} | {val:.14f}       | {error:.4e}           | {improvement}")

# --- 4. Uruchomienie ---
tasks = [
    ("a)", f1, -1, 7, exact_f1()),
    ("b)", f2, -1, 1, exact_f2()),
    ("c)", f3, 0, 5, exact_f3())
]

for t in tasks:
    show_diagonal_path(*t)