#!/usr/bin/python
import spidev
import time

WRITE_FLAG = (1<<7)
REG_TCOOLTHRS = 0x14
REG_GCONF = 0x00
REG_IHOLD_IRUN = 0x10
REG_CHOPCONF = 0x6C

TCOOLTHRS_REF = 0x00000001
#AIN_CUR_REF = 0x00000001
AIN_CUR_REF_D0STALL = 0x00001081
IHOLD_IRUN = 0x00001010
USTEP = 0x00008008

NUM=${1}

spi = spidev.SpiDev()
spi.open(32766, 0)
spi.max_speed_hz = 3000000
spi.mode = 0b11

data0 = [WRITE_FLAG | REG_TCOOLTHRS, (TCOOLTHRS_REF >> 24) & 0xFF,(TCOOLTHRS_REF >> 16) & 0xFF,(TCOOLTHRS_REF >> 8) & 0xFF, TCOOLTHRS_REF & 0xFF]
to_send0 = data0
for i in range(2, NUM):
	to_send0 += data0

resp = spi.xfer(to_send1,3000000,0,8)
print resp

data1 = [WRITE_FLAG | REG_GCONF, (AIN_CUR_REF_D0STALL >> 24) & 0xFF,(AIN_CUR_REF_D0STALL >> 16) & 0xFF,(AIN_CUR_REF_D0STALL >> 8) & 0xFF, AIN_CUR_REF_D0STALL & 0xFF]
to_send1 = data1
for i in range(2, NUM):
	to_send1 += data1

resp = spi.xfer(to_send1,3000000,0,8)
print resp

data2 = [WRITE_FLAG | REG_IHOLD_IRUN, (IHOLD_IRUN >> 24) & 0xFF,(IHOLD_IRUN >> 16) & 0xFF,(IHOLD_IRUN >> 8) & 0xFF, IHOLD_IRUN & 0xFF]
to_send2 = data2
for i in range(2, NUM):
	to_send2 += data2

resp = spi.xfer2(to_send2,3000000,1,8)
print resp

data3 = [WRITE_FLAG | REG_CHOPCONF, (USTEP >> 24) & 0xFF,(USTEP >> 16) & 0xFF,(USTEP >> 8) & 0xFF, USTEP & 0xFF]
to_send3 = data3
for i in range(2, NUM):
	to_send3 += data3

resp = spi.xfer2(to_send3,3000000,1,8)
print resp



spi.close()
