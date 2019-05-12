# Python3 SPI
For mksocfpga cramps stepper trinamic spi configuration

initial setup:

    sudo apt install python3-pip
    pip3 install spidev
    git clone https://github.com/the-snowwhite/PYSPI.git

run width:

    /home/machinekit/PYSPI/set_tmc2130.sh (num of daisy chained sstep drivers)

    or

    /home/machinekit/PYSPI/set_tmc2660.sh (num of daisy chained sstep drivers)
