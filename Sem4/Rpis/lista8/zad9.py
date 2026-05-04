import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# 1. Przygotowanie osi X (prawdopodobieństwo p od 0 do 1)
x = np.linspace(0, 1, 500)

# 2. Obliczenie gęstości dla naszych trzech rozkładów
# A priori
y_prior = beta.pdf(x, 10, 10)

# A posteriori 1 (1 sukces, 4 porażki w 5 próbach)
y_post1 = beta.pdf(x, 11, 14)

# A posteriori 2 (4 sukcesy, 1 porażka w 5 próbach)
y_post2 = beta.pdf(x, 14, 11)

# 3. Rysowanie wykresu
plt.figure(figsize=(10, 6))

# Dodajemy krzywe
plt.plot(x, y_prior, label='A priori: Beta(10, 10)', linestyle='--', color='gray', linewidth=2)
plt.plot(x, y_post1, label='A post. 1 (n=5, k=1): Beta(11, 14)', color='blue', linewidth=2)
plt.plot(x, y_post2, label='A post. 2 (n=5, k=4): Beta(14, 11)', color='red', linewidth=2)

# Formatowanie wykresu
plt.title('Aktualizacja rozkładu Beta po zebraniu danych')
plt.xlabel('Prawdopodobieństwo sukcesu (p)')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.legend()
plt.grid(True, alpha=0.3)

# Wyświetlenie
plt.show()