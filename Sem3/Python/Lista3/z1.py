import math
import timeit

def pierwsze_imperatywne(n):
    pierwsze = []
    for i in range(2, n+1):
        if(czyPierwsza(i)):
            pierwsze.append(i)
    return pierwsze

def pierwsze_funkcyjna(n):
    return list(filter(lambda x: czyPierwsza(x), range(2, n+1)))

def pierwsze_skladana(n):
    return [i for i in range(2, n+1) if czyPierwsza(i)]

def czyPierwsza(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Pomiary czasu
def zmierz_czas(func, n, repeats=100):
    """Mierzy czas wykonania funkcji używając timeit"""
    return timeit.timeit(lambda: func(n), number=repeats) / repeats

print(pierwsze_imperatywne(1000))
print (pierwsze_imperatywne(1000) == pierwsze_skladana(1000) == pierwsze_funkcyjna(1000))
# Wyświetl tabelkę z wynikami
print("n\tskladana\timperatywna\tfunkcyjna")
print("="*60)

wartosci_n = [10, 20, 50, 100, 200, 500, 1000]

for n in wartosci_n:
    czas_skladana = zmierz_czas(pierwsze_skladana, n)
    czas_imperatywna = zmierz_czas(pierwsze_imperatywne, n)
    czas_funkcyjna = zmierz_czas(pierwsze_funkcyjna, n)
    
    print(f"{n:<4}\t{czas_skladana:.6f}\t{czas_imperatywna:.6f}\t\t{czas_funkcyjna:.6f}")