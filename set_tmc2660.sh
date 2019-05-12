#!/bin/bash

NUM=${1}
# socfpga_cyclone5_de0_sockit.dtb
GNUM=465
# socfpga_cyclone5_de10_nano_uio_fb_hd.dtb
#GNUM=369

sudo sh -c 'echo "'${GNUM}'" > /sys/class/gpio/export'
sudo sh -c 'echo "out" > /sys/class/gpio/gpio'${GNUM}'/direction'
sudo sh -c 'echo "0" > /sys/class/gpio/gpio'${GNUM}'/value'
sudo sh -c 'chmod 666 /dev/spidev32765.0'
cd ~/PYSPI
python3 /home/machinekit/PYSPI/Set_tmc2660_x-256-step.py ${NUM}
