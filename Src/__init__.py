import numpy as np
from minimos_quadrados.minimos_quadrados import perform_mq as minimos_quadrados
from simpson13.simpson13_graph import perform_13 as simpson13
from simpson38.simpson38_graph import perform38 as simpson38
from trapezio.trapezio import plotar_trapezios as trapezio

# Função base
funcao_base = "np.sin(x)**2"

# Simpson 1/3
# python main.py simpson13
# Deve ser par
numero_13 = 6
simpson13(funcao_base, 0, np.pi, numero_13)

# Simpson 3/8
# python main.py simpson38
# Deve ser um múltiplo de 3
numero_38 = 6
simpson38(funcao_base, 0, np.pi, numero_38)

# Trapézio Generalizado
# python main.py trapezio
# Comporta qualquer número
numero_trapezio = 6
trapezio(funcao_base, 0, np.pi, numero_trapezio)

# Mínino Quadrado
# python main.py minimos_quadrados
numero_mq = 6
minimos_quadrados(funcao_base, 0, np.pi, numero_mq)