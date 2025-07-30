#!/bin/sh
ARQUIVODADOS=/home/pi/sist_embarcados_git/lab07/gnuplot/dados4.txt
ARQUIVOSAIDA=/home/pi/sist_embarcados_git/lab07/gnuplot/dados4.png

gnuplot << EOF
set title "Gráfico Equação de Terceiro Grau"
set ylabel "Eixo Y"
set xlabel "Eixo X"
set terminal png
set output "$ARQUIVOSAIDA"
plot "$ARQUIVODADOS" \
     linecolor rgb '#eb34df' \
     linetype 1 \
     linewidth 1 \
     pointtype 2 \
     pointsize 1.0 \
     title "meus dados" \
     with linespoints
EOF

