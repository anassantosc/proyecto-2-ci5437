import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

negamaxExpanded = [0, 1, 3, 1, 6, 7, 49, 98, 575, 2361, 6244, 37532, 222933, 1781833, 6548613, 44595493, 436519885, 2805093090, 2843083336]
negamaxAlphaBetaExpanded = [0, 1, 3, 1, 6, 7, 14, 22, 77, 138, 238, 426, 949, 5331, 8159, 13108, 30889, 72013, 334738, 389659, 372637, 449219, 898837, 1254326, 1180827, 730743, 1857653, 1130083, 4464751, 2180235, 2031118, 1122764, 663227, 683100]
scoutExpanded = [0, 1, 2, 1, 3, 4, 5, 6, 7, 64, 14, 52, 20, 35, 43, 117, 115, 185, 10858, 1908, 28382, 103, 47264, 855, 85666, 16, 20508, 16, 76, 153, 88, 302, 16, 1089]
negascoutExpanded = [0, 1, 3, 1, 9, 10, 11, 38, 213, 264, 477, 1096, 1762, 22528, 29874, 52428, 205413, 72013, 3248391, 4366467, 10944215, 16921708, 15949519, 77379173, 60019008, 16247776, 59571885, 46099086, 155726579, 65781778, 49990410, 17892399, 31081221, 19681752]

negamaxExpanded = np.log([1+x for x in negamaxExpanded])
negamaxAlphaBetaExpanded = np.log([1+x for x in negamaxAlphaBetaExpanded])
scoutExpanded = np.log([1+x for x in scoutExpanded])
negascoutExpanded = np.log([1+x for x in negascoutExpanded])

plt.plot(negamaxExpanded, label='Negamax')
plt.plot(negamaxAlphaBetaExpanded, label='Negamax Alfa Beta')
plt.plot(scoutExpanded, label='Scout')
plt.plot(negascoutExpanded, label='Negascout')

plt.xlabel('Niveles PV')
plt.ylabel('Logaritmo de Nodos Expandidos')
plt.title('Valor asintótico de los Nodos Expandidos por cada nivel PV')
plt.legend()
plt.savefig('Expanded.png')
