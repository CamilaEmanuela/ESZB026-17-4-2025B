#!/bin/sh
ARQUIVODADOS=/home/pi/sist_embarcados_git/lab07/gnuplot/dados3.txt
ARQUIVOSAIDA=/home/pi/sist_embarcados_git/lab07/gnuplot/dados3.png

gnuplot << EOF
set title "Gráfico Equação de Segundo Grau"
set ylabel "Eixo Y"
set xlabel "Eixo X"
set terminal png
set output "$ARQUIVOSAIDA"
plot "$ARQUIVODADOS" \
     linecolor rgb '#34bdeb' \
     linetype 0.95 \
     linewidth 0.95 \
     pointtype 1.5 \
     pointsize 1.5 \
     title "meus dados" \
     with linespoints
EOF

