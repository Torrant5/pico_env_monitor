from machine import Pin, I2C
import time
from ccs811 import CCS811
from bme280 import BME280
from sht35 import SHT35



i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
i2c1 = I2C(1, scl=Pin(15, Pin.PULL_UP), sda=Pin(14, Pin.PULL_UP), freq=10000)
address0 = i2c0.scan()
address1 = i2c1.scan()
print("temp & humid & atom-----")
print(address0)
print(hex(address0[0]))
print(hex(address0[1]))

print("CO2---------------------")
print(address1)
print(hex(address1[0]))

sht = SHT35(i2c = i2c0)
bme = BME280(i2c = i2c0)
ccs = CCS811(i2c1)
ccs.setup()

while True:
    if ccs.data_available():
        ccs_r = ccs.read_algorithm_results()
        sht_r = sht.read_data()
        bme_r = bme.values
        #print("CO2:{}, tVOC:{}, TEMP:{}({}), HUMID:{}({}), PRESSURE:{}".format(ccs_r[0], ccs_r[1], sht_r[0], bme_r[0], sht_r[1], bme_r[2], bme_r[1]))
        #print("CO2:{}, tVOC:{}, TEMP:{}, HUMID:{}, PRESSURE:{}".format(ccs_r[0], ccs_r[1], sht_r[0], sht_r[1], bme_r[1]))
        print("{}, {}, {}, {}, {}".format(ccs_r[0], ccs_r[1], sht_r[0], sht_r[1], bme_r[1]))
    else:
        print("waiting...")
    time.sleep(2)