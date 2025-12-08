import numpy as np
import matplotlib.pyplot as plt

class FastNIFS3:

    def __init__(self, nodes):
        self.t = np.array(nodes, dtype=float) # punkty
        self.n = len(nodes) - 1 #ilosc punktow
        self.h = np.diff(self.t) #tablica h
        

        self.alpha = np.zeros(self.n) # Alphu
        self.denominators = np.zeros(self.n) # Mianowniki 
        self.lambdas = np.zeros(self.n)      # Lambdy


        for k in range(1, self.n):
            self.lambdas[k] = self.h[k] / (self.h[k] + self.h[k+1]) if k < self.n - 1 else 0
            
            # mianownik = 2 + lambda_k * alpha_{k-1}
            # alpha_k = (lambda_k - 1) / mianownik
            
            denom = 2 + self.lambdas[k] * self.alpha[k-1]
            self.denominators[k] = denom
            
            if k < self.n - 1: # alpha liczymy do n-2, bo M_n=0
                self.alpha[k] = (self.lambdas[k] - 1) / denom

    def get_moments(self, y):
        
        y = np.array(y, dtype=float)
        M = np.zeros(self.n + 1)
        beta = np.zeros(self.n)
        

        for k in range(1, self.n):
            # f[x_k-1,x_k,x_k+1]
            diff_div_1 = (y[k] - y[k-1]) / self.h[k-1]      # f[x_k-1, x_k]
            diff_div_2 = (y[k+1] - y[k]) / self.h[k]        # f[x_k, x_k+}]
            second_diff = (diff_div_2 - diff_div_1) / (self.h[k-1] + self.h[k])
            #prawa strona układu rownań
            d_k = 6 * second_diff
            
            # beta_k = (d_k - lambda_k * beta_{k-1}) / mianownik
            beta[k] = (d_k - self.lambdas[k] * beta[k-1]) / self.denominators[k]

        #Liczymy m 
        M[self.n] = 0
        
        for k in range(self.n - 1, 0, -1):
            # M_k = alpha_k * M_{k+1} + beta_k
            M[k] = self.alpha[k] * M[k+1] + beta[k]
            
        return M

    def evaluate_spline(self, y, M, u_points):

        results = []
        # Liczymy splajny z wzoru a + b(x-xk) + c(x-xk)^2 + d(x-xk)^3
        for u in u_points:
            #szukamy przedziału
            k = np.searchsorted(self.t, u, side='right') - 1 
            k = max(0, min(k, self.n - 1))
            

            h = self.h[k] 
            dx = u - self.t[k] # x - xk
            
            a = y[k]
            b = (y[k+1] - y[k])/h - h*(2*M[k] + M[k+1])/6.0
            c = M[k] / 2.0
            d = (M[k+1] - M[k]) / (6.0 * h)
            
            val = a + b*dx + c*(dx**2) + d*(dx**3)
            results.append(val)
            
        return np.array(results)

# --- DANE Z ZADANIA L8.7 ---

# Węzły t_k = k/95
t_nodes = np.linspace(0, 1, 96) # 0, 1/95, ..., 95/95=1 

# Dane X (przepisane z treści zadania)
X_data = [
    5.5, 8.5, 10.5, 13, 17, 20.5, 24.5, 28, 32.5, 37.5, 40.5, 42.5, 45, 47,
    49.5, 50.5, 51, 51.5, 52.5, 53, 52.8, 52, 51.5, 53, 54, 55, 56, 55.5, 54.5, 54, 55, 57, 58.5,
    59, 61.5, 62.5, 63.5, 63, 61.5, 59, 55, 53.5, 52.5, 50.5, 49.5, 50, 51, 50.5, 49, 47.5, 46,
    45.5, 45.5, 45.5, 46, 47.5, 47.5, 46, 43, 41, 41.5, 41.5, 41, 39.5, 37.5, 34.5, 31.5, 28, 24,
    21, 18.5, 17.5, 16.5, 15, 13, 10, 8, 6, 6, 6, 5.5, 3.5, 1, 0, 0, 0.5, 1.5, 3.5, 5, 5, 4.5, 4.5, 5.5,
    6.5, 6.5, 5.5
]

# Dane Y (przepisane z treści zadania)
Y_data = [
    41, 40.5, 40, 40.5, 41.5, 41.5, 42, 42.5, 43.5, 45, 47, 49.5, 53, 57, 59,
    59.5, 61.5, 63, 64, 64.5, 63, 61.5, 60.5, 61, 62, 63, 62.5, 61.5, 60.5, 60, 59.5, 59, 58.5,
    57.5, 55.5, 54, 53, 51.5, 50, 50, 50.5, 51, 50.5, 47.5, 44, 40.5, 36, 30.5, 28, 25.5, 21.5,
    18, 14.5, 10.5, 7.50, 4, 2.50, 1.50, 2, 3.50, 7, 12.5, 17.5, 22.5, 25, 25, 25, 25.5, 26.5,
    27.5, 27.5, 26.5, 23.5, 21, 19, 17, 14.5, 11.5, 8, 4, 1, 0, 0.5, 3, 6.50, 10, 13, 16.5, 20.5,
    25.5, 29, 33, 35, 36.5, 39, 41
]

# --- URUCHOMIENIE ALGORYTMU ---

# 1. Inicjalizacja "silnika" splajnu (Etap I - wykonywany RAZ)
splines = FastNIFS3(t_nodes)

# 2. Obliczenie momentów dla X i Y (Etap II - wykonywany wielokrotnie)
Mx = splines.get_moments(X_data)
My = splines.get_moments(Y_data)

# 3. Siatka punktów do generowania obrazka - 1000 punktów w przedziale [0,1]
u = np.linspace(0, 1, 1000)

# 4. Tworzymy splajny dla x i y
sx_vals = splines.evaluate_spline(X_data, Mx, u)
sy_vals = splines.evaluate_spline(Y_data, My, u)

# Rysujemy obrazek
plt.figure(figsize=(8, 8))
plt.plot(sx_vals, sy_vals, 'b-', linewidth=2, label='NIFS3 Parametryczna')
plt.axis('equal') # Ważne, żeby zachować proporcje rysunku!
plt.grid(True)
plt.show()