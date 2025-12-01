import numpy as np
import matplotlib.pyplot as plt

def cheb_nodes(n):
    k = np.arange(0,n+1)
    return np.cos((2*k+1)*np.pi/(2*(n+1)))

xs = np.linspace(-1,1,1000)
for n in range(4,21):

    x_eq = np.linspace(-1,1,n+1)
    p_eq = np.ones_like(xs)
    for xi in x_eq: p_eq *= (xs - xi)

    x_ch = cheb_nodes(n)
    p_ch = np.ones_like(xs)
    for xi in x_ch: p_ch *= (xs - xi)

    plt.figure(figsize=(8,3))
    plt.plot(xs, p_eq, label='równoodległe')
    plt.plot(xs, p_ch, label='Czebyszewa', linestyle='--')
    plt.axhline(0,color='k',linewidth=0.5)
    plt.title(f"p_{{{n+1}}}(x) dla n={n}")
    plt.legend()
    plt.show()
