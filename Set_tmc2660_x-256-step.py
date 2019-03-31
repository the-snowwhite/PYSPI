
#!/usr/bin/python
import spidev
import time
import sys

REG_DRVCTRL  = (0<<7)
REG_CHOPCONF = (4<<17)
REG_SMARTEN  =  (5<<7)
REG_SGCSCONF = (6<<7)
REG_DRVCONF  = (7<<7)

CHOPCONF = 0x00001

NUM=int(sys.argv[1])

spi = spidev.SpiDev()
spi.open(32765, 0)
spi.max_speed_hz = 3000000
spi.mode = 0b11
spi.bits_per_word = 8

#data1 = [ (REG_CHOPCONF | (CHOPCONF >> 10)) & 0x3FF, CHOPCONF & 0x3FF , 0x0]
data1 = [ (REG_CHOPCONF | CHOPCONF ) ]
to_send1 = data1
#for i in range(2, NUM):
#	to_send1 += data1

#xfer3(list of values[, speed_hz, delay_usec, bits_per_word])
#resp = spi.xfer2(to_send1,3000000,0,8)
resp = spi.xfer3(to_send1,3000000,0,20)
resp = spi.xfer2(to_send1)
print resp

#data2 = [WRITE_FLAG | REG_IHOLD_IRUN, (IHOLD_IRUN >> 24) & 0xFF,(IHOLD_IRUN >> 16) & 0xFF,(IHOLD_IRUN >> 8) & 0xFF, IHOLD_IRUN & 0xFF]
#to_send2 = data2
#for i in range(2, NUM):
#	to_send2 += data2

#resp = spi.xfer2(to_send2,3000000,1,8)
#print resp

#data3 = [WRITE_FLAG | REG_CHOPCONF, (USTEP >> 24) & 0xFF,(USTEP >> 16) & 0xFF,(USTEP >> 8) & 0xFF, USTEP & 0xFF]
#to_send3 = data3
#for i in range(2, NUM):
#	to_send3 += data3

#resp = spi.xfer2(to_send3,3000000,1,8)
#print resp


spi.close()
