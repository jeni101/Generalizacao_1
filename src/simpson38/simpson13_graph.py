# integral = h / 3 * [f(x0) + 4 * f(x1) +  f(x2)]
# com repetição precisa de nummero impar de pontos ou nuero par de intervalos
# "" = h / 3 * [f(X0) + 4 * f(x impar) +  2 * f(X par) + f(Xn)]
# intervalos são medidos pelo x0 e xfinal, (xf-x0)/n2 = h
#ponto intermediario x1 = (xfinal+x0)


import numpy as np
import matplotlib.pyplot as plt

def simpson13_vector(y, h):
   
    n = len(y) - 1  
    
   
    if n % 2 != 0:
        raise ValueError(f"Simpson 1/3 requer n par de intervalos. Recebido: {n}")

   
    weights = np.ones(n + 1)
    weights[1:-1:2] = 4  
    weights[2:-1:2] = 2  

    return (h / 3) * np.dot(weights, y)

def perform_simpson13(f_str, a, b, n_max):
   
    
    n_values = np.arange(2, n_max + 1, 2)
    resultados = []
    
    for n in n_values:
        x = np.linspace(a, b, n + 1)  
        h = (b - a) / n
        
        
        try:
            y = eval(f_str, {"__builtins__": None}, {"np": np, "x": x})
            resultados.append(simpson13_vector(y, h))
        except Exception as e:
            print(f"Erro ao avaliar a função: {e}")
            return

    
    resultados = np.array(resultados)
    ref_val = resultados[-1]  
    erros_residuais = np.abs(resultados[:-1] - ref_val)
    n_para_erro = n_values[:-1]

    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    
    ax1.plot(n_values, resultados, 'o-', color='#1f77b4', label='Integral Calculada')
    ax1.axhline(y=ref_val, color='r', linestyle='--', alpha=0.5, label='Valor Estabilizado')
    ax1.set_title(f"Convergência Simpson 1/3 para: {f_str}")
    ax1.set_ylabel("Valor da Integral")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

   
    ax2.semilogy(n_para_erro, erros_residuais, 's-', color='#9467bd', label='Erro $|I_n - I_{ref}|$')
    ax2.set_title("Análise de Erro (Decaimento da Imprecisão)")
    ax2.set_xlabel("Número de Intervalos (n) - Somente Pares")
    ax2.set_ylabel("Erro Absoluto")
    ax2.legend()
    ax2.grid(True, which="both", ls="-", alpha=0.2)

    plt.tight_layout()
    plt.show()

