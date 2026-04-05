import numpy as np
from simpson38.simpson38_graph import perform

# Simpson 3/8
# python main.py perform
# Função base
funcao_simpson = "np.sin(x)**2"
# Deve ser um múltiplo de 3
numero = 999
perform(funcao_simpson, 0, np.pi, numero)