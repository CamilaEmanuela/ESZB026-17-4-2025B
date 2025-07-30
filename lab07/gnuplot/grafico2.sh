#!/bin/sh
ARQUIVODADOS=/home/pi/sist_embarcados_git/lab07/gnuplot/dados2.txt
ARQUIVOSAIDA=/home/pi/sist_embarcados_git/lab07/gnuplot/dados2.png

gnuplot << EOF
set title "Título"
set ylabel "Eixo Y"
set xlabel "Eixo X"
set terminal png
set output "$ARQUIVOSAIDA"
plot "$ARQUIVODADOS" \
     linecolor rgb '#FF0000' \
     linetype 2 \
     linewidth 4 \
     pointtype 1 \
     pointsize 2.0 \
     title "meus dados 2" \
     with linespoints
EOF

