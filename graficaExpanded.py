import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

negamaxExpanded = [0, 1, 3, 1, 6, 7, 49, 98, 575, 2361, 6244, 37532, 222933, 1781833, 6548613, 44595493, 436519885, 2805093090]
negamaxAlphaBetaExpanded = [0, 1, 3, 1, 6, 7, 17, 25, 147, 381, 999, 3631, 6728, 61859, 88527, 173194, 1029920, 1535491, 16194511, 34643976, 69179931, 320632162, 3224251, 3464038517, 1879244970]
scoutExpanded = [0, 1, 2, 1, 8, 9, 13, 28, 151, 175, 749, 467, 2940, 12583, 53642, 78268, 209350, 537207, 2526372, 4136289, 18027214, 38740608, 520878670, 1131568553]
negascoutExpanded = [0, 1, 3, 1, 9, 10, 11, 38, 213, 264, 477, 1096, 1762, 22528, 29874, 52428, 205413, 381374, 3380066, 16992650, 54098487, 97552015, 816134204, 1319457904, 1888020125, 2499872789]

plt.plot(negamaxExpanded, label='Negamax')
plt.plot(negamaxAlphaBetaExpanded, label='Negamax Alfa Beta')
plt.plot(scoutExpanded, label='Scout')
plt.plot(negascoutExpanded, label='Negascout')

plt.xlabel('Niveles PV')
plt.ylabel('Logaritmo de Nodos Expandidos')
plt.title('Valor asintótico de los Nodos Expandidos por cada nivel PV')
plt.legend()
plt.savefig('Expanded.png')
