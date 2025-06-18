#!/usr/bin/python3

import sys
from time import sleep

def writeLED ( filename, value, path ):
	"Esta funcao escreve o valor 'value' no arquivo 'path+filename'"
	fo = open( path + filename,"w")
	fo.write(value)
	fo.close()
	return
	
for i in range(5):
	 print(f"--- Running iteration {i+1}/5 ---")


print("Export....")
writeLED (filename="export", value="21", path="/sys/class/gpio/")
writeLED (filename="export", value="20", path="/sys/class/gpio/")
writeLED (filename="export", value="16", path="/sys/class/gpio/")

print("Direction....")

writeLED (filename="direction", value="out", path="/sys/class/gpio/gpio21/")
writeLED (filename="direction", value="out", path="/sys/class/gpio/gpio20/")
writeLED (filename="direction", value="out", path="/sys/class/gpio/gpio16/")


print("Ligando....")


writeLED (filename="value", value="1", path="/sys/class/gpio/gpio20/")
sleep(2)
writeLED (filename="value", value="0", path="/sys/class/gpio/gpio20/")



writeLED (filename="value", value="1", path="/sys/class/gpio/gpio21/")
sleep(1)
writeLED (filename="value", value="0", path="/sys/class/gpio/gpio21/")

writeLED (filename="value", value="1", path="/sys/class/gpio/gpio16/")
sleep(1)
writeLED (filename="value", value="0", path="/sys/class/gpio/gpio16/")

print("Unexport....")


writeLED (filename="unexport", value="21", path="/sys/class/gpio/")
writeLED (filename="unexport", value="20", path="/sys/class/gpio/")
writeLED (filename="unexport", value="16", path="/sys/class/gpio/")



print(f"--- Finished iteration {i+1}/5 ---\n")
