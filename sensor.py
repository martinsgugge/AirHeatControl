import smbus
from time import sleep
import os
import glob

def tc74():

    channel = 1
    address = 0x48

    bus = smbus.SMBus(channel)

    data = bus.read_byte(address)
    data = data*5.0/9.0

    return data


class ds18b20:
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    def __init__(self):
        pass

    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            #temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c

if __name__ == '__main__':
    ds18b20 = ds18b20()
    while True:
        print(ds18b20.read_temp())
        print(tc74())
