#!/bin/bash

# Definindo os caminhos dos arquivos de entrada e saída
ARQUIVODADOS="/var/www/html/dados_arduino.txt"
ARQUIVOSAIDA="/tmp/dados_arduino.png"

# Executa o Gnuplot com as configurações de plotagem
gnuplot << EOF
    set title "Tí tulo"
    set ylabel "Eixo Y"
    set xlabel "Eixo X"
    set terminal png
    set output "$ARQUIVOSAIDA"
    plot "$ARQUIVODADOS" \
        linecolor rgb '#0060ad' \
        linetype 1 \
        linewidth 1 \
        pointtype 2 \
        pointsize 1.0 \
        title "meus dados" \
        with linespoints
EOF
