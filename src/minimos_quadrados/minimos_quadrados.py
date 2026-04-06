import numpy as np
import matplotlib.pyplot as plt

def minimos_quadrados(x, y):
    n = len(x)

    a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
        (n * np.sum(x**2) - (np.sum(x))**2)

    b = (np.sum(y) - a * np.sum(x)) / n

    return a, b

def perform_mq(x, y):
    a, b = minimos_quadrados(x, y)

    y_fit = a * x + b
    erro = np.abs(y - y_fit)

    _plotar_resultados(x, y, y_fit, erro)

def _plotar_resultados(x, y, y_fit, erro):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.plot(x, y, 'o-', label='Dados')
    ax1.plot(x, y_fit, '-', label='Ajuste MQ')
    ax1.set_title("Mínimos Quadrados")
    ax1.legend()

    ax2.plot(x, erro, 's-r', label='Erro Residual')
    ax2.set_title("Erro")
    ax2.legend()

    plt.tight_layout()
    plt.show()