#!/usr/bin/python 
import spidev
import time

WRITE_FLAG = (1<<7) 
REG_GCONF = 0x00 
REG_IHOLD_IRUN = 0x10
REG_CHOPCONF = 0x6C

AIN_CUR_REF = 0x00000001
IHOLD_IRUN = 0x00001010
USTEP = 0x00008008

spi = spidev.SpiDev()
spi.open(32766, 0)
spi.max_speed_hz = 3000000
spi.mode = 0b11

to_send = [WRITE_FLAG | REG_GCONF, (AIN_CUR_REF >> 24) & 0xFF,(AIN_CUR_REF >> 16) & 0xFF,(AIN_CUR_REF >> 8) & 0xFF, AIN_CUR_REF & 0xFF]
resp = spi.xfer(to_send,3000000,0,8)
print resp

to_send = [WRITE_FLAG | REG_IHOLD_IRUN, (IHOLD_IRUN >> 24) & 0xFF,(IHOLD_IRUN >> 16) & 0xFF,(IHOLD_IRUN >> 8) & 0xFF, IHOLD_IRUN & 0xFF]
resp = spi.xfer2(to_send,3000000,1,8)
print resp

to_send = [WRITE_FLAG | REG_CHOPCONF, (USTEP >> 24) & 0xFF,(USTEP >> 16) & 0xFF,(USTEP >> 8) & 0xFF, USTEP & 0xFF]
resp = spi.xfer2(to_send,3000000,1,8)
print resp



spi.close()
