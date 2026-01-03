import numpy as np
import matplotlib.pyplot as plt


class FastNIFS3:

    def __init__(self, nodes):
        self.t = np.array(nodes, dtype=float)  # punkty
        self.n = len(nodes) - 1  # ilosc punktow
        self.h = np.diff(self.t)  # tablica h

        self.alpha = np.zeros(self.n)  # Alphy
        self.denominators = np.zeros(self.n)  # Mianowniki
        self.lambdas = np.zeros(self.n)  # Lambdy

        for k in range(1, self.n):
            self.lambdas[k] = (
                self.h[k] / (self.h[k] + self.h[k + 1]) if k < self.n - 1 else 0
            )

            # mianownik = 2 + lambda_k * alpha_{k-1}
            # alpha_k = (lambda_k - 1) / mianownik

            denom = 2 + self.lambdas[k] * self.alpha[k - 1]
            self.denominators[k] = denom

            if k < self.n - 1:  # alpha liczymy do n-2, bo M_n=0
                self.alpha[k] = (self.lambdas[k] - 1) / denom

    def get_moments(self, y):

        y = np.array(y, dtype=float)
        M = np.zeros(self.n + 1)
        beta = np.zeros(self.n)

        for k in range(1, self.n):
            # f[x_k-1,x_k,x_k+1]
            diff_div_1 = (y[k] - y[k - 1]) / self.h[k - 1]  # f[x_k-1, x_k]
            diff_div_2 = (y[k + 1] - y[k]) / self.h[k]  # f[x_k, x_k+}]
            second_diff = (diff_div_2 - diff_div_1) / (self.h[k - 1] + self.h[k])
            # prawa strona układu rownań
            d_k = 6 * second_diff

            # beta_k = (d_k - lambda_k * beta_{k-1}) / mianownik
            beta[k] = (d_k - self.lambdas[k] * beta[k - 1]) / self.denominators[k]

        # Liczymy m
        M[self.n] = 0

        for k in range(self.n - 1, 0, -1):
            # M_k = alpha_k * M_{k+1} + beta_k
            M[k] = self.alpha[k] * M[k + 1] + beta[k]

        return M

    def evaluate_spline(self, y, M, u_points):

        results = []
        # Liczymy splajny z wzoru a + b(x-xk) + c(x-xk)^2 + d(x-xk)^3
        for u in u_points:
            # szukamy przedziału
            k = np.searchsorted(self.t, u, side="right") - 1
            k = max(0, min(k, self.n - 1))

            h = self.h[k]
            dx = u - self.t[k]  # x - xk

            a = y[k]
            b = (y[k + 1] - y[k]) / h - h * (2 * M[k] + M[k + 1]) / 6.0
            c = M[k] / 2.0
            d = (M[k + 1] - M[k]) / (6.0 * h)

            val = a + b * dx + c * (dx**2) + d * (dx**3)
            results.append(val)

        return np.array(results)

