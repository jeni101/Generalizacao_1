import numpy as np
from simpson38.simpson38_graph import perform38 as simpson38
from simpson13.simpson13_graph import perform_13 as simpson13

# Função base
funcao_simpson = "np.sin(x)**2"

# Simpson 1/3
# python main.py simpson13
# Deve ter número de intervalos par
numero_13 = 9
simpson13(funcao_simpson, 0, np.pi, numero_13)

# Simpson 3/8
# python main.py simpson38
# Deve ser um múltiplo de 3
numero_38 = 9
simpson38(funcao_simpson, 0, np.pi, numero_38)