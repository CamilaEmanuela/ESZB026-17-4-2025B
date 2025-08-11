#!/usr/bin/python3

import serial
import time

conexaoSerial = serial.Serial( '/dev/ttyACM0' ,115200)
time.sleep(2)


def ler_um_dado():
	if (conexaoSerial.inWaiting() > 0):
		dado_recebido = conexaoSerial.read_until(b'\n')
		return dado_recebido
	else:
		return -2


for i in range(20):
	dado_lido = ler_um_dado()
	valor = int(dado_lido)
	print(valor)
	time.sleep(0.5)




# programas:
# 1) prog1: vai comunicar com o Arduino, pegar as medidas e gravar um arquivo .txt
#  ex lab7: /usr/local/bin/le_pot_spi
#
# 2) prog2: vai mostrar a página web:
#  ex lab7: /usr/lib/cgi-bin/le_pot_spi.cgi, que vai estar em /usr/lib/cgi-bin/
#  - esse programa vai chamar o prog1 e o prog3
#
# 3) prog3: mostra a imagem web:
#  ex lab7: /usr/lib/cgi-bin/imagem_spi.cgi
#  - esse programa chama um scrit que lê o txt e cria o gráfico (prog4)
#
# 4) prog4: lê o txt e cria o gráfico
# ex lab7: /usr/local/bin/grafico_spi.sh
#
# prog1, prog4, prog3, prog2
