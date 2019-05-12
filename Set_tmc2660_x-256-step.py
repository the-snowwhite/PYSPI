
#!/usr/bin/python
import spidev
import time
import sys

REG_DRVCTRL  = 0x0
REG_CHOPCONF = 0x8
REG_SMARTEN  = 0xA
REG_SGCSCONF = 0xC
REG_DRVCONF  = 0xE

# Hysteresis mode
#CHOPCONF = 0x101B4
CHOPCONF = 0x101B8

# Constant toff mode
#CHOPCONF = 0x14557

# Current setting: $d001F (max. current)
#SGCSCONF = 0x1001F

#SGCSCONF = 0x10016
SGCSCONF = 0x10016

SGCSCONF_Z = 0x1001F

# low driver strength, stallGuard2 read, SDOFF=0
DRVCONF  = 0x00010

# 256 microstep setting
DRVCTRL  = 0x00000

# coolStep:
SMARTEN = 0x08202

NUM=int(sys.argv[1])

spi = spidev.SpiDev()
spi.open(32765, 0)
spi.max_speed_hz = 3000000
spi.mode = 0b11
spi.bits_per_word = 8


def send_list( num, reg, list_data ):
    data1 = [ (reg  | (list_data >> 16)) & 0xF, (list_data >> 12) & 0xF, (list_data >> 8) & 0xF, (list_data >> 4) & 0xF, list_data & 0xF ]

    if (num % 2) == 1:
        data = [ data1[0] ,
        (data1[1] << 4) | data1[2],
        (data1[3] << 4) | data1[4] ]
        to_send1 = data

    if ((num % 2) == 0) or (num > 2):
        data = [ (data1[0] << 4) | (data1[1] ) ,
        (data1[2] << 4) | data1[3],
        (data1[4] << 4) | data1[0] ,
        (data1[1] << 4) | data1[2] ,
        (data1[3] << 4) | data1[4] ]
        if (num % 2) == 0:
            to_send1 = data
        else:
            to_send1 += data

        for i in range(3, num,2):
            to_send1 += data

    resp = spi.xfer2(to_send1,3000000,0,8)
    for idx, val in enumerate(resp):
        high, low = (val >> 4) & 0xF, val & 0xF
        if (idx == 0):
            v_data = [high, low]
        else:
            v_data += [high, low]

    if (NUM % 2) == 1:
        inx = 1
    else:
        inx = 0

    p_data = v_data[inx:inx+5]
    for y in range(1, NUM):
        p_data += v_data[((y*5)+inx):((y*5)+inx+5)]


    print("p_data = ",[hex(x) for x in p_data])
    print("p_data = ",[bin(x) for x in p_data])
    print("")

send_list(NUM, REG_CHOPCONF, CHOPCONF)
send_list(NUM, REG_SGCSCONF, SGCSCONF)
#send_list(NUM, REG_SGCSCONF, SGCSCONF_Z)
send_list(NUM, REG_DRVCONF, DRVCONF)
send_list(NUM, REG_DRVCTRL, DRVCTRL)
send_list(NUM, REG_SMARTEN, SMARTEN)



spi.close()
