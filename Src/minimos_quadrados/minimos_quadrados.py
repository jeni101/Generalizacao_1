import numpy as np
import matplotlib.pyplot as plt

def minimos_quadrados(x, y):
    n = len(x)

    a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
        (n * np.sum(x**2) - (np.sum(x))**2)

    b = (np.sum(y) - a * np.sum(x)) / n

    return a, b

def perform_mq(f_str, inicio, fim, n):
    x = np.linspace(inicio, fim, n)
    
    y = eval(f_str, {"__builtins__": None}, {"np": np, "x": x})
    
    # Chama o cálculo original
    a, b = minimos_quadrados(x, y)

    y_fit = a * x + b
    erro = np.abs(y - y_fit)

    _plotar_resultados(x, y, y_fit, erro)
    
    return a, b

def _plotar_resultados(x, y, y_fit, erro):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    ax1.plot(x, y, 'o', label='Dados Originais', color='darkblue')
    ax1.plot(x, y_fit, '-', label='Ajuste MQ (Reta)', color='red')
    ax1.set_title("Mínimos Quadrados: Ajuste Linear")
    ax1.set_ylabel("Eixo Y")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(x, erro, 's-r', label='Erro Residual $|y_{real} - y_{fit}|$')
    ax2.set_title("Análise de Erro Residual")
    ax2.set_xlabel("Eixo X")
    ax2.set_ylabel("Erro Absoluto")
    ax2.legend()
    ax2.grid(True, which="both", ls="-", alpha=0.2)

    plt.tight_layout()
    plt.show()