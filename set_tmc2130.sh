#!/bin/bash

NUM=${1}

sudo sh -c 'echo "465" > /sys/class/gpio/export'
sudo sh -c 'echo "out" > /sys/class/gpio/gpio465/direction'
#sudo sh -c 'echo "1" > /sys/class/gpio/gpio465/value'
sudo sh -c 'chmod 666 /dev/spidev32766.0'
cd ~/SPI
python /home/machinekit/SPI/Set_tmc2130_x-256-step.py ${NUM}
