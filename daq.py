from scaling import Scaler

import nidaqmx
from nidaqmx.constants import (
        TerminalConfiguration)

class DAQ:
    def __init__(self, type, channel,low=1, high=5):
        self.type = type
        self.channel = channel
        self.low = low
        self.high = high

    def create_channel(self):
        if self.IO_type == 'Input':
            if self.type == 'RSE':
                self.task = nidaqmx.Task()
                self.task.ai_channels.add_ai_voltage_chan(self.channel, min_val=self.low, max_val=self.high,
                                                     terminal_config=TerminalConfiguration.RSE)
                self.task.start()
            elif self.type == 'Differential':
                self.task = nidaqmx.Task()
                self.task.ai_channels.add_ai_voltage_chan(self.channel, min_val=self.low, max_val=self.high,
                                                     terminal_config=TerminalConfiguration.DIFFERENTIAL)
                self.task.start()
        elif self.IO_type == 'Output':

            self.task = nidaqmx.Task()
            self.task.ao_channels.add_ao_voltage_chan(self.channel, min_val=self.low, max_val=self.high,)
            self.task.start()

    def close_channel(self):
        self.task.stop()
        self.task.close()


class Sensor(DAQ):


    def __init__(self, name, type, channel, low_in, high_in, low_out, high_out):
        self.IO_type = 'Input'
        self.name = name

        self.type = type
        self.channel = channel
        self.low = low_in
        self.high = high_in

        self.create_channel()

        self.low_out = low_out
        self.high_out = high_out

        self.scaler = Scaler(low_in, high_in, low_out, high_out)

    def read(self):
        self.task.read()
        print(self.task.read())
        self.y = self.scaler.convert(self.task.read())

class Actuator(DAQ):
    def __init__(self, name, channel, low_in, high_in, low_out, high_out):
        self.IO_type = 'Output'
        self.name = name

        self.channel = channel
        self.low = low_in
        self.high = high_in

        self.create_channel()

        self.low_out = low_out
        self.high_out = high_out

        self.scaler = Scaler(low_in, high_in, low_out, high_out)

    def write(self, value):
        value = self.scaler.convert(value)
        self.task.write(value)







