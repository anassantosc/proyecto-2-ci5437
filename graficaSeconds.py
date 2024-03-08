import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

negamaxSeconds = [1.00024e-06, 6.99982e-06, 2.99979e-06, 9.99775e-07, 4.99981e-06, 3.00026e-06, 1.89999e-05, 4.10001e-05, 0.000197, 0.000832, 0.002108, 0.013115, 0.077227, 0.621852, 2.26065, 15.4569, 152.546, 996.899]
negamaxAlphaBetaSeconds = [9.99775e-07, 1.99955e-06, 2.00002e-06, 9.99775e-07, 2.00002e-06, 2.00002e-06, 4.00003e-06, 6.00005e-06, 3.3e-05, 8.40002e-05, 0.000198, 0.000786, 0.001448, 0.025632, 0.038983, 0.075911, 0.475626, 0.698836, 7.4296, 16.6768, 32.5574, 173.038, 676.026, 1938.65, 3454.18]
scoutSeconds = [1.99955e-06, 5.00027e-06, 2.99979e-06, 1.00024e-06, 6.99982e-06, 6.99982e-06, 8.99937e-06, 2.50004e-05, 0.000121, 0.000171, 0.000681, 0.000493, 0.002946, 0.013398, 0.057635, 0.087097, 0.315409, 0.647099, 3.35677, 5.35708, 23.9705, 50.2478, 648.2, 1450.82]
negascoutSeconds = [2.00002e-06, 4.00003e-06, 3.9998e-06, 1.00001e-06, 5.00004e-06, 7.99983e-06, 9.00007e-06, 1.90001e-05, 9.5e-05, 0.000127, 0.000279, 0.000692, 0.00095, 0.011225, 0.021321, 0.028755, 0.106787, 0.2136, 1.94793, 10.0145, 32.1805, 58.3955, 478.144, 779.431, 1123.22, 1505.92]

plt.plot(negamaxSeconds, label='Negamax')
plt.plot(negamaxAlphaBetaSeconds, label='Negamax Alfa Beta')
plt.plot(scoutSeconds, label='Scout')
plt.plot(negascoutSeconds, label='Negascout')

plt.xlabel('Niveles PV')
plt.ylabel('Logaritmo de Tiempo en Segundos por cada nivel')
plt.title('Valor asintótico del Tiempo por cada nivel PV')
plt.legend()
plt.savefig('Time.png')
