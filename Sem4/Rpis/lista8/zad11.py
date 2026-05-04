import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.stats import gamma

# Inicjalne wartości parametrów
init_p = 4.0      # kształt a priori (p)
init_b = 1.0      # tempo a priori (b)
init_n = 10       # liczba obserwacji z modelu Poissona
init_sum_x = 30   # suma zaobserwowanych wartości

# Tworzenie głównego okna i wykresu
fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(bottom=0.35) # Robimy miejsce na suwaki na dole

# Oś X
x = np.linspace(0.01, 20, 1000)

# Obliczanie początkowych gęstości
# W scipy.stats.gamma parametr 'a' to kształt, a 'scale' to 1/tempo
y_prior = gamma.pdf(x, a=init_p, scale=1/init_b)
y_post = gamma.pdf(x, a=init_p + init_sum_x, scale=1/(init_b + init_n))

# Rysowanie krzywych
line_prior, = ax.plot(x, y_prior, 'k--', label=f'A priori: Gamma({init_b:.1f}, {init_p:.1f})', lw=2, alpha=0.6)
line_post, = ax.plot(x, y_post, 'b-', label=f'A posteriori: Gamma({init_b+init_n:.1f}, {init_p+init_sum_x:.1f})', lw=2)

ax.set_title('Aktualizacja Bayesowska: Model Poissona + A priori Gamma')
ax.set_xlabel(r'Wartość parametru $\xi$')
ax.set_ylabel('Gęstość prawdopodobieństwa')
ax.legend()
ax.grid(True, alpha=0.3)

# Definicja obszarów na suwaki (lewo, dół, szerokość, wysokość)
ax_p = plt.axes([0.15, 0.25, 0.65, 0.03])
ax_b = plt.axes([0.15, 0.20, 0.65, 0.03])
ax_n = plt.axes([0.15, 0.15, 0.65, 0.03])
ax_sum_x = plt.axes([0.15, 0.10, 0.65, 0.03])

# Tworzenie suwaków
slider_p = Slider(ax_p, 'Kształt (p)', 1.0, 20.0, valinit=init_p)
slider_b = Slider(ax_b, 'Tempo (b)', 0.1, 10.0, valinit=init_b)
slider_n = Slider(ax_n, 'Liczba prób (n)', 1.0, 50.0, valinit=init_n, valstep=1)
slider_sum_x = Slider(ax_sum_x, 'Suma obs. (Σx)', 0.0, 150.0, valinit=init_sum_x, valstep=1)

# Funkcja odświeżająca wykres po przesunięciu suwaka
def update(val):
    p = slider_p.val
    b = slider_b.val
    n = slider_n.val
    sum_x = slider_sum_x.val
    
    # Nowe parametry a posteriori
    post_p = p + sum_x
    post_b = b + n
    
    # Dostosowanie osi X, by wykres się nie uciął przy dużych wartościach
    max_val = max(p/b, post_p/post_b) * 2.5
    max_val = max(max_val, 5) 
    x_new = np.linspace(0.01, max_val, 1000)
    
    # Nowe gęstości
    new_y_prior = gamma.pdf(x_new, a=p, scale=1/b)
    new_y_post = gamma.pdf(x_new, a=post_p, scale=1/post_b)
    
    # Aktualizacja danych na wykresie
    line_prior.set_xdata(x_new)
    line_prior.set_ydata(new_y_prior)
    line_prior.set_label(f'A priori: Gamma({b:.1f}, {p:.1f})')
    
    line_post.set_xdata(x_new)
    line_post.set_ydata(new_y_post)
    line_post.set_label(f'A posteriori: Gamma({post_b:.1f}, {post_p:.1f})')
    
    # Skalowanie osi
    ax.set_xlim(0, max_val)
    max_y = max(np.max(new_y_prior), np.max(new_y_post))
    ax.set_ylim(0, max_y * 1.1)
    
    ax.legend()
    fig.canvas.draw_idle()

# Podpięcie zdarzeń - przesunięcie suwaka wywołuje funkcję update
slider_p.on_changed(update)
slider_b.on_changed(update)
slider_n.on_changed(update)
slider_sum_x.on_changed(update)

# Wyświetlenie interaktywnego okna
plt.show()