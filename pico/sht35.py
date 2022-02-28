from machine import Pin, I2C
import time

_ADDR = 0x45

class SHT35:
    def __init__(self, i2c: I2C):
        self._i2c = i2c
        
    def decode_temp(self, msb, lsb, csc):
        divnum = 65535 #2-16-1
        s = ((msb<<8 )| lsb)
        T = -45 + 175 * s/divnum
        return T

    def decode_humid(self, msb, lsb, csc):
        divnum = 65535 #2-16-1
        s = ((msb<<8 )| lsb)
        RH = 100 * s/divnum
        return RH
    
    def read_data(self):
        self._i2c.writeto(_ADDR, b'\x2C\x06')
        data = self._i2c.readfrom(_ADDR, 6)
        
        data_li = [d for d in data]

        temp = self.decode_temp(*data_li[0:3])
        humid = self.decode_humid(*data_li[3:6])
        return (temp, humid)
    

