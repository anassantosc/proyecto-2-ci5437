#!/bin/bash

make

echo "Ejecutando con profundidad $1 con tabla de transposicion"
./main 1 false >> ./salidas/negamax/p$1.txt
./main 2 false >> ./salidas/negamax-poda/p$1.txt
./main 3 false >> ./salidas/scout/p$1.txt
# ./main 4 false >> ./salidas/negascout/p$1.txt



