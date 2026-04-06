from minimos_quadrados import perform_mq
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 4.0, 5.9, 8.2, 10.1])

perform_mq(x, y)