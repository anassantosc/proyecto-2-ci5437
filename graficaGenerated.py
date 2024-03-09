import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

negamaxGenerated = [0, 1, 4, 0, 7, 8, 66, 130, 754, 3173, 7959, 48266, 287306, 2263734, 8358060, 57894111, 574629641, 3708262376, 1403098391]
negamaxAlphaBetaGenerated = [0, 1, 4, 0, 7, 8, 16, 25, 90, 159, 279, 486, 1119, 6198, 9769, 15396, 37190, 85961, 446095, 640609, 573241, 807788, 1468338, 2561823, 2209719, 1472737, 3128514, 2453079, 7649905, 5948080, 3813820, 2216301, 1314690, 1364623]
scoutGenerated = [0, 1, 3, 0, 5, 6, 9, 11, 16, 133, 27, 114, 44, 101, 95, 328, 212, 467, 22934, 6107, 90331, 290, 185366, 3541, 418300, 101, 107914, 108, 386, 865, 445, 1898, 77, 6464]
negascoutGenerated = [0, 1, 4, 0, 9, 10, 11, 42, 244, 318, 564, 1286, 2063, 26779, 35766, 62336, 248175, 85961, 4699390, 7567543, 19247119, 34463220, 34714704, 177350880, 151235463, 36912269, 152551897, 126308007, 418761041, 202342423, 131569207, 55716580, 94155587, 61625034]

negamaxGenerated = np.log([1+x for x in negamaxGenerated])
negamaxAlphaBetaGenerated = np.log([1+x for x in negamaxAlphaBetaGenerated])
scoutGenerated = np.log([1+x for x in scoutGenerated])
negascoutGenerated = np.log([1+x for x in negascoutGenerated])

plt.plot(negamaxGenerated, label='Negamax')
plt.plot(negamaxAlphaBetaGenerated, label='Negamax Alfa Beta')
plt.plot(scoutGenerated, label='Scout')
plt.plot(negascoutGenerated, label='Negascout')

plt.xlabel('Niveles PV')
plt.ylabel('Logaritmo de Nodos Generados')
plt.title('Valor asintótico de los Nodos Generados por cada nivel PV')
plt.legend()
plt.savefig('Generated.png')

