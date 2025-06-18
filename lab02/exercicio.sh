#!/bin/bash

echo '\e[47;33;1m Comeco \e[m'

echo 20 > /sys/class/gpio/export
echo 21 > /sys/class/gpio/export
echo 16 > /sys/class/gpio/export

echo out > /sys/class/gpio/gpio20/direction
echo out > /sys/class/gpio/gpio21/direction
echo out > /sys/class/gpio/gpio16/direction


for i in $(seq 5); do 

echo 1 > /sys/class/gpio/gpio20/value
sleep 2
echo 0 > /sys/class/gpio/gpio20/value

echo 1 > /sys/class/gpio/gpio21/value
sleep 1
echo 0 > /sys/class/gpio/gpio21/value

echo 1 > /sys/class/gpio/gpio16/value
sleep 1
echo 0 > /sys/class/gpio/gpio16/value

done


echo 20 > /sys/class/gpio/unexport
echo 21 > /sys/class/gpio/unexport
echo 16 > /sys/class/gpio/unexport

echo '\e[42;31;1m FIM \e[m'
