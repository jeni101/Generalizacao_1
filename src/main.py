import numpy as np
from simpson38.simpson38_graph import perform
from simpson38.simpson13_graph import perform_13

# Simpson 3/8
# python main.py perform
# Função base
funcao_simpson = "np.sin(x)**2"
# Deve ser um múltiplo de 3
numero = 999
perform(funcao_simpson, 0, np.pi, numero)

numero_13 = 1000
perform_13(funcao_simpson, 0, np.pi, numero_13)