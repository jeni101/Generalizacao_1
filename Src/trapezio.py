import numpy as np
import matplotlib.pyplot as plt 

# =========================
# Função que calcula a integral usando o método dos trapézios
# =========================


def calcular_integral_trapezio(funcao, inicio, fim, quantidade_de_trapezios):
   
    # Calcula a largura de cada trapézio
    largura = (fim - inicio) / quantidade_de_trapezios
    
    # Cria os pontos de avaliação igualmente espaçados
    pontos = np.linspace(inicio, fim, quantidade_de_trapezios + 1)
    
    # Avalia a função nesses pontos
    valores = funcao(pontos)
    
    # Soma os valores das extremidades e dobra os valores intermediários
    soma = valores[0] + valores[-1] + 2 * sum(valores[1:-1])
    
    # Calcula a integral aproximada
    integral = (largura / 2) * soma 
    
    
    return integral, pontos, valores 



# =========================
# Função que plota a função e os trapézios
# =========================

def plotar_trapezios(funcao, inicio, fim, quantidade_de_trapezios):
    # Calcula a integral e os pontos/valores usando a função anterior
    integral, pontos, valores = calcular_integral_trapezio(funcao, inicio, fim, quantidade_de_trapezios)
    
    # Cria pontos mais finos para desenhar a curva da função 
    pontos_suaves = np.linspace(inicio, fim, 1000)
    valores_suaves = funcao(pontos_suaves)
    
    # Plota a curva da função
    plt.plot(pontos_suaves, valores_suaves, label="Função")
    
    # Desenha os trapézios preenchendo a área sob a curva
    for i in range(quantidade_de_trapezios):
        plt.fill(
            [pontos[i], pontos[i], pontos[i + 1], pontos[i + 1]],  # coordenadas x do trapézio
            [0, valores[i], valores[i + 1], 0],                    # coordenadas y do trapézio
            alpha=0.3                                                # transparência para visualizar a curva
        )
    
    # Configurações do gráfico
    plt.title(f"Integral aproximada = {integral:.4f}")  # mostra o valor da integral no título
    plt.xlabel("x")                                     # legenda do eixo x
    plt.ylabel("f(x)")                                  # legenda do eixo y
    plt.legend()                                        # adiciona legenda
    plt.grid()                                          # adiciona grid
    plt.show()                                          # exibe o gráfico
    
    
    return integral