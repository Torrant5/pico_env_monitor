import serial
import time, datetime

ser = serial.Serial('COM3', 9600) #Windows
# ser = serial.Serial('/dev/ttyACM0', 115200) #Raspberry Pi

interval = 10

# filepath = "../host_front/pico-env-monitor/public/log/today.csv"
filepath = "../host_front/pico-env-monitor/dist/log/today.csv"

try:
    with open(filepath, mode='x') as f:
        f.write("TIME, TEMP, HUMID, PRESSURE, CO2\n")
except FileExistsError:
    pass

print("TEMP, HUMID, PRESSURE, CO2\n")

while True:        
    data = ser.readline()
    s = [ss.strip(" \r\n") for ss in data.decode().split(",")]
    t = f"{datetime.datetime.now():%H:%M:%S}"
    print("{}, {}, {}, {}, {}".format(*s))
    
    with open(filepath, 'a') as f:
        print("{}, {}, {}, {}, {}".format(t, *s), file=f)
    
    time.sleep(interval)
    