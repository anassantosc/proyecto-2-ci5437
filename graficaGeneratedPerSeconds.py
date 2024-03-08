import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

negamaxGeneratedPerSeconds = [0, 142861, 1.33343e+06, 0, 1.40005e+06, 2.66644e+06, 3.4737e+06, 3.17073e+06, 3.82741e+06, 3.8137e+06, 3.77562e+06, 3.68021e+06, 3.72028e+06, 3.64031e+06, 3.69719e+06, 3.74551e+06, 3.76693e+06, 3.7198e+06]
negamaxAlphaBetaGeneratedPerSeconds = [0, 500113, 1.99998e+06, 0, 3.49997e+06, 3.99997e+06, 4.99996e+06, 4.8333e+06, 5.39394e+06, 5.61904e+06, 6.06062e+06, 5.56489e+06, 5.63398e+06, 2.89236e+06, 2.7543e+06, 2.77451e+06, 2.67116e+06, 2.70834e+06, 2.73935e+06, 2.6181e+06, 2.67763e+06, 2.33903e+06, 7587.68, 35049.6, 1.01251e+06]
scoutGeneratedPerSeconds = [0, 199989, 1.33343e+06, 0, 1.28575e+06, 1.42861e+06, 2.00014e+06, 2.11996e+06, 2.52066e+06, 2.40351e+06, 2.55947e+06, 2.36917e+06, 2.3425e+06, 2.33983e+06, 2.40677e+06, 2.29626e+06, 1.79568e+06, 2.14775e+06, 2.05564e+06, 2.11835e+06, 2.17594e+06, 2.21567e+06, 2.28875e+06, 2.20123e+06]
negascoutGeneratedPerSeconds = [0, 249998, 1.00005e+06, 0, 1.79999e+06, 1.25003e+06, 1.22221e+06, 2.21051e+06, 2.56842e+06, 2.50394e+06, 2.02151e+06, 1.85838e+06, 2.17158e+06, 2.38566e+06, 1.6775e+06, 2.16783e+06, 2.32402e+06, 2.15686e+06, 2.15114e+06, 2.11895e+06, 2.07151e+06, 2.06685e+06, 2.10243e+06, 2.10203e+06, 2.09113e+06, 2.06513e+06]

plt.plot(negamaxGeneratedPerSeconds, label='Negamax')
plt.plot(negamaxAlphaBetaGeneratedPerSeconds, label='Negamax Alfa Beta')
plt.plot(scoutGeneratedPerSeconds, label='Scout')
plt.plot(negascoutGeneratedPerSeconds, label='Negascout')

plt.xlabel('Niveles PV')
plt.ylabel('Logaritmo de Nodos Generados por Segundos')
plt.title('Valor asintótico de los Nodos Generados por Segundos por cada nivel PV')
plt.legend()
plt.savefig('GeneratePerSg.png')


