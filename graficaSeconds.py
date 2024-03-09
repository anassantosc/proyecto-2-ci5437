import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

negamaxSeconds = [2.99979e-06, 1.40001e-05, 1.20001e-05, 4.00003e-06, 1.80001e-05, 1.89999e-05, 7.20001e-05, 9.99998e-05, 0.000846, 0.001861, 0.004427, 0.022815, 0.111078, 0.891311, 3.21021, 22.723, 219.021, 1381.66, 6468.32]
negamaxAlphaBetaSeconds = [2.00002e-06, 3.00002e-06, 4.00003e-06, 1.00001e-06, 6.00005e-06, 5.00004e-06, 1.20001e-05, 1.69999e-05, 5.7e-05, 0.000101, 0.000175, 0.00038, 0.000669, 0.003722, 0.005614, 0.008963, 0.02062, 0.047394, 0.228578, 0.326137, 0.31838, 0.462886, 0.932153, 1.61061, 1.57749, 1.08983, 2.75942, 1.6897, 6.69309, 3.5194, 3.38367, 1.91627, 1.11328, 1.14843]
scoutSeconds = [1.00001e-06, 7.00005e-06, 6.00005e-06, 3.00002e-06, 1.00001e-05, 1.09999e-05, 1.20001e-05, 1.40001e-05, 1.70001e-05, 6.90001e-05, 2.7e-05, 7.30001e-05, 3.80001e-05, 9.5e-05, 6.99998e-05, 0.000181, 0.000132, 0.000236, 0.009386, 0.002651, 0.041442, 0.000175003, 0.067329, 0.001317, 0.152251, 5.89788e-05, 0.04056, 5.90086e-05, 0.000155985, 0.000432998, 0.000212014, 0.000687987, 5.79953e-05, 0.00186601]
negascoutSeconds = [2.00002e-06, 2.99991e-06, 4.00003e-06, 1.00001e-06, 6.00005e-06, 6.00005e-06, 6.99994e-06, 2.6e-05, 0.00016, 0.000182, 0.00051, 0.000801, 0.00121, 0.015461, 0.019887, 0.036616, 0.134747, 0.047394, 2.48989, 3.69677, 9.75385, 17.4437, 17.4318, 97.2611, 82.7526, 23.459, 89.2308, 72.8675, 254.882, 115.036, 86.1313, 34.1503, 59.608, 40.877]

negamaxSeconds = np.log([1+x for x in negamaxSeconds])
negamaxAlphaBetaSeconds = np.log([1+x for x in negamaxAlphaBetaSeconds])
scoutSeconds = np.log([1+x for x in scoutSeconds])
negascoutSeconds = np.log([1+x for x in negascoutSeconds])  

plt.plot(negamaxSeconds, label='Negamax')
plt.plot(negamaxAlphaBetaSeconds, label='Negamax Alfa Beta')
plt.plot(scoutSeconds, label='Scout')
plt.plot(negascoutSeconds, label='Negascout')

plt.xlabel('Niveles PV')
plt.ylabel('Logaritmo de Tiempo en Segundos por cada nivel')
plt.title('Valor asintótico del Tiempo por cada nivel PV')
plt.legend()
plt.savefig('Time.png')
