import numpy as np
import matplotlib.pyplot as plt

def simpson38(y, h):
    n = len(y) - 1
    if n % 3 != 0:
        raise ValueError("Para o Método de Simpson 3/8, 'n' deve ser múltiplo de 3.")
    
    weights = np.ones(n + 1)
    weights[1:-1:3] = 3
    weights[2:-1:3] = 3
    weights[3:-1:3] = 2
    
    return (3 * h / 8) * np.sum(weights * y)

def perform38(f_str, a, b, n_max):
    safe_dict = {"np": np, "x": None}
    
    n_values = np.arange(3, n_max + 1, 3)
    resultados = []
    
    for n in n_values:
        x = np.linspace(a, b, n + 1)
        h = (b - a) / n
        
        y = eval(f_str, {"__builtins__": None}, {"np": np, "x": x})
        resultados.append(simpson38(y, h))

    ref_val = resultados[-1]
    erros_residuais = [abs(res - ref_val) for res in resultados[:-1]]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    ax1.plot(n_values, resultados, 'o-', color='darkblue', label='Resultado $I(n)$')
    ax1.axhline(y=ref_val, color='red', linestyle='--', alpha=0.6, label='Valor Estabilizado')
    ax1.set_title(f"Convergência de Simpson 3/8 para: {f_str}")
    ax1.set_ylabel("Resultado da Integral")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.semilogy(n_values[:-1], erros_residuais, 's-', color='darkorange', label='Erro Residual $|I_n - I_{max}|$')
    ax2.set_title("Análise de Erro Residual (Escala Logarítmica)")
    ax2.set_xlabel("Número de Segmentos (n)")
    ax2.set_ylabel("Erro Absoluto")
    ax2.legend()
    ax2.grid(True, which="both", ls="-", alpha=0.2)

    plt.tight_layout()
    plt.show()

# funcao = "np.sin(x)**2"
# perform(funcao, 0, np.pi, 90)