import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

negamaxGeneratedPerSeconds = [0, 71428, 333331, 0, 388886, 421055, 916666, 1.3e+06, 891253, 1.705e+06, 1.79783e+06, 2.11554e+06, 2.58652e+06, 2.53978e+06, 2.60359e+06, 2.54782e+06, 2.62362e+06, 2.68392e+06, 216918]
negamaxAlphaBetaGeneratedPerSeconds = [0, 333331, 999992, 0, 1.16666e+06, 1.59999e+06, 1.33332e+06, 1.4706e+06, 1.57895e+06, 1.57426e+06, 1.59429e+06, 1.27895e+06, 1.67265e+06, 1.66523e+06, 1.74011e+06, 1.71773e+06, 1.80359e+06, 1.81375e+06, 1.95161e+06, 1.96423e+06, 1.80049e+06, 1.74511e+06, 1.57521e+06, 1.59059e+06, 1.40078e+06, 1.35135e+06, 1.13376e+06, 1.45178e+06, 1.14296e+06, 1.69008e+06, 1.12712e+06, 1.15657e+06, 1.18091e+06, 1.18825e+06]
scoutGeneratedPerSeconds = [0, 142856, 499996, 0, 499996, 545462, 749994, 785708, 941169, 1.92753e+06, 1e+06, 1.56164e+06, 1.15789e+06, 1.06316e+06, 1.35715e+06, 1.81215e+06, 1.60606e+06, 1.97881e+06, 2.44343e+06, 2.30366e+06, 2.1797e+06, 1.65711e+06, 2.75314e+06, 2.68868e+06, 2.74744e+06, 1.71248e+06, 2.6606e+06, 1.83024e+06, 2.47459e+06, 1.9977e+06, 2.09892e+06, 2.75877e+06, 1.32769e+06, 3.46407e+06]
negascoutGeneratedPerSeconds = [0, 333344, 999992, 0, 1.49999e+06, 1.66665e+06, 1.57144e+06, 1.61539e+06, 1.525e+06, 1.74725e+06, 1.10588e+06, 1.60549e+06, 1.70496e+06, 1.73204e+06, 1.79846e+06, 1.70243e+06, 1.84178e+06, 1.81375e+06, 1.88739e+06, 2.04707e+06, 1.97329e+06, 1.97568e+06, 1.99146e+06, 1.82345e+06, 1.82756e+06, 1.57348e+06, 1.70963e+06, 1.73339e+06, 1.64296e+06, 1.75895e+06, 1.52754e+06, 1.63151e+06, 1.57958e+06, 1.50757e+06]

negamaxGeneratedPerSeconds = np.log([1+x for x in negamaxGeneratedPerSeconds])
negamaxAlphaBetaGeneratedPerSeconds = np.log([1+x for x in negamaxAlphaBetaGeneratedPerSeconds])    
scoutGeneratedPerSeconds = np.log([1+x for x in scoutGeneratedPerSeconds])
negascoutGeneratedPerSeconds = np.log([1+x for x in negascoutGeneratedPerSeconds])

plt.plot(negamaxGeneratedPerSeconds, label='Negamax')
plt.plot(negamaxAlphaBetaGeneratedPerSeconds, label='Negamax Alfa Beta')
plt.plot(scoutGeneratedPerSeconds, label='Scout')
plt.plot(negascoutGeneratedPerSeconds, label='Negascout')

plt.xlabel('Niveles PV')
plt.ylabel('Logaritmo de Nodos Generados por Segundos')
plt.title('Valor asintótico de los Nodos Generados por Segundos por cada nivel PV')
plt.legend()
plt.savefig('GeneratePerSg.png')


