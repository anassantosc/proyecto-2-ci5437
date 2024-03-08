import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

negamaxGenerated = [0, 1, 4, 0, 7, 8, 66, 130, 754, 3173, 7959, 48266, 287306, 2263734, 8358060, 57894111, 574629641, 3708262376]
negamaxAlphaBetaGenerated = [0, 1, 4, 0, 7, 8, 20, 29, 178, 472, 1200, 4374, 8158, 74137, 107371, 210616, 1270471, 1892683, 20352253, 43661622, 87176788, 404741432, 5129464, 67948849, 3497406762]
scoutGenerated = [0, 1, 4, 0, 9, 10, 18, 53, 305, 411, 1743, 1168, 6901, 31349, 138714, 199997, 566373, 1389809, 6900309, 11348148, 52158453, 111332522, 1483565490, 3193588664]
negascoutGenerated = [0, 1, 4, 0, 9, 10, 11, 42, 244, 318, 564, 1286, 2063, 26779, 35766, 62336, 248175, 460706, 4190261, 21220286, 66662224, 120694553, 1005264618, 1638389048, 2348800529, 3109932267]

plt.plot(negamaxGenerated, label='Negamax')
plt.plot(negamaxAlphaBetaGenerated, label='Negamax Alfa Beta')
plt.plot(scoutGenerated, label='Scout')
plt.plot(negascoutGenerated, label='Negascout')

plt.xlabel('Niveles PV')
plt.ylabel('Logaritmo de Nodos Generados')
plt.title('Valor asintótico de los Nodos Generados por cada nivel PV')
plt.legend()
plt.savefig('Generated.png')

