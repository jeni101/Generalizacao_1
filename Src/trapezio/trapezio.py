import numpy as np
import matplotlib.pyplot as plt 

# =========================
# Função que calcula a integral usando o método dos trapézios
# =========================

def calcular_integral_trapezio(f_str, inicio, fim, quantidade_de_trapezios):
    
    # Calcula a largura de cada trapézio
    largura = (fim - inicio) / quantidade_de_trapezios
    
    # Cria os pontos de avaliação igualmente espaçados
    # (Adaptado para usar 'x' para compatibilidade com o eval do main.py)
    x = np.linspace(inicio, fim, quantidade_de_trapezios + 1)
    
    # Avalia a função nesses pontos usando eval para processar a string vinda do main.py
    valores = eval(f_str, {"__builtins__": None}, {"np": np, "x": x})
    
    # Soma os valores das extremidades e dobra os valores intermediários
    # Usei np.sum para manter a performance com arrays do numpy
    soma = valores[0] + valores[-1] + 2 * np.sum(valores[1:-1])
    
    # Calcula a integral aproximada
    integral = (largura / 2) * soma 
    
    return integral, x, valores 

# =========================
# Função que plota a análise de convergência e erro (Novo Padrão)
# =========================

def plotar_trapezios(f_str, inicio, fim, n_max):
    # O Trapézio comporta qualquer número de intervalos (n >= 1)
    n_values = np.arange(1, n_max + 1)
    resultados = []
    
    # Loop para coletar os resultados de n=1 até n_max
    for n in n_values:
        # Chama sua função original de cálculo
        integral, _, _ = calcular_integral_trapezio(f_str, inicio, fim, n)
        resultados.append(integral)

    # Define o valor de referência como o último resultado (n_max)
    ref_val = resultados[-1]
    # Calcula o erro absoluto em relação ao valor mais preciso alcançado
    erros_residuais = [abs(res - ref_val) for res in resultados[:-1]]

    # Criação da figura com dois subplots (Convergência e Erro)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    # --- Subplot 1: Gráfico de Convergência ---
    ax1.plot(n_values, resultados, 'o-', color='darkgreen', label='Resultado $I(n)$')
    ax1.axhline(y=ref_val, color='red', linestyle='--', alpha=0.6, label='Valor Estabilizado')
    ax1.set_title(f"Convergência de Trapézio Generalizado para: {f_str}")
    ax1.set_ylabel("Resultado da Integral")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # --- Subplot 2: Gráfico de Erro Residual (Escala Logarítmica) ---
    ax2.semilogy(n_values[:-1], erros_residuais, 's-', color='seagreen', label='Erro Residual $|I_n - I_{max}|$')
    ax2.set_title("Análise de Erro Residual (Escala Logarítmica)")
    ax2.set_xlabel("Número de Segmentos (n)")
    ax2.set_ylabel("Erro Absoluto")
    ax2.legend()
    ax2.grid(True, which="both", ls="-", alpha=0.2)

    # Ajusta o layout e exibe o gráfico final
    plt.tight_layout()
    plt.show()
    
    return ref_val