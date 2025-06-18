echo Boa tarde!

echo 21 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio21/direction
echo 16 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio16/direction


echo 1 > /sys/class/gpio/gpio21/value
sleep 2
echo 0 > /sys/class/gpio/gpio21/value
sleep 1

echo 1 > /sys/class/gpio/gpio16/value
sleep 2
echo 0 > /sys/class/gpio/gpio16/value
sleep 1

echo 1 > /sys/class/gpio/gpio21/value
sleep 2
echo 0 > /sys/class/gpio/gpio21/value
sleep 1



echo 21 > /sys/class/gpio/unexport
echo 16 > /sys/class/gpio/unexport
