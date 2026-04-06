
import numpy as np
import trapezio 
import limpar_tela  

#imformations

def ajuda_sintaxe():
    print("""|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                 COMO DIGITAR A FUNÇÃO                       |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| USE SEMPRE: x como variável                                 |
| Exemplo: x**2, x**3 + 2*x                                   |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| FUNÇÕES DISPONÍVEIS (direto, sem np.):                      |
| sin(x)   → seno                                             |
| cos(x)   → cosseno                                          |
| exp(x)   → exponencial                                      |
| log(x)   → logaritmo natural                                |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| EXEMPLOS VÁLIDOS:                                           |
| x**2                                                        |
| x**3 + 2*x                                                  |
| sin(x)                                                      |
| x**2 + cos(x)                                               |
| exp(x) + x                                                  |
| log(x) + x**2                                               |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| ERROS COMUNS:                                               |
| ❌ sin(4)        → não depende de x                         |
| ❌ x^2           → use x**2                                 |
| ❌ sen(x)        → use sin(x)                               |
| ❌ faltar *       → ex: 2x → use 2*x                        |
| ❌ usar np.sin(x) → não precisa do np.                      |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| DICA: sempre use x dentro da função!                        |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
""")

# =========================
# FORMATAÇÃO P USUÁRIO 
# =========================
def funcao(x):
    return eval(func_str, {
        "x": x,
        "sin": np.sin,
        "cos": np.cos,
        "exp": np.exp,
        "log": np.log
    })

# =========================
# FORMATAÇÃO DE TEXTO
# =========================

def formatar(texto, tamanho=30):
    return str(texto)[:tamanho].ljust(tamanho)

# =========================
# MENSAGEM FINAL
# =========================

def mensagem(func_str, inicio, fim, n, resultado):
    print(f"""|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|FUNÇÃO: {formatar(func_str)}
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|INICIO DO INTERVALO: {formatar(inicio)}
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|FIM DO INTERVALO: {formatar(fim)}
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|NUMERO DE TRAPEZIOS: {formatar(n)}
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|RESULTADO: {formatar(f"{resultado:.4f}")}
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
""")

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    limpar_tela.limpar_tela()  
    ajuda_sintaxe()
    
    func_str = input("Digite a função desejada:\n\n")
    print("")
    
    inicio = float(input("Digite o início do intervalo: "))
    print("")
    
    fim = float(input("Digite o fim do intervalo: "))
    print("")
    
    n = int(input("Quantidade de trapézios: "))
    print("")
    
    #calcula integral
    resultado, _, _ = trapezio.calcular_integral_trapezio(funcao, inicio, fim, n)

    limpar_tela.limpar_tela()
    mensagem(func_str, inicio, fim, n, resultado)

    #gráfico
    trapezio.plotar_trapezios(funcao, inicio, fim, n)