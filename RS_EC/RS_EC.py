# RS PRO Conductivity Meter readout
# By Jochem van der Meulen 

import serial

class SensorError(Exception):
    pass

class ecMeter():
    def __init__(self, port):
        self.uart = serial.Serial(port=port, baudrate=9600, timeout=1.5)

    def read(self):
        self.uart.reset_input_buffer()

        # read sensor
        self.tries = 3
        while 1:
            self.msg = self.uart.read_until(expected=b'\r').decode()
            if len(self.msg) == 16:
                break
            if self.tries == 1:
                raise SensorError("device not responding")
            self.tries -= 1

        # decode polarity
        match int(self.msg[1]):
            case 0:
                self.pUp  =  1
                self.pLow =  1
            case 1:
                self.pUp  = -1
                self.pLow =  1
            case 2:
                self.pUp  =  1
                self.pLow = -1
            case 3:
                self.pUp  = -1
                self.pLow = -1

        # decode upper display unit
        match int(self.msg[3:5]):
            case 1:
                self.upUnit = "C"
            case 2:
                self.upUnit = "F"
            case 13:
                self.upUnit = "uS"
            case 14:
                self.upUnit = "mS"

        #decode lower display unit
        match int(self.msg[2]):
            case 0:
                self.lowUnit = "noUnit"
            case 1:
                self.lowUnit = "C"
            case 2:
                self.lowUnit = "F"

        #decode upper display value
        if self.msg[11] == '\x19':
            self.upValue = float('nan') # value to low
        elif self.msg[11] == '\x18':
            self.upValue = float('nan') # value to high
        else:
            self.upValue = (float(self.msg[11:15]) / pow(10, int(self.msg[6]))) * self.pUp
            

        #decode lower display value
        if self.msg[7] == '\x19':
            self.lowValue = float('nan') # value to low
        elif self.msg[7] == '\x18':
            self.lowValue = float('nan') # value to high
        else:
            self.lowValue = (float(self.msg[ 7:11]) / pow(10, int(self.msg[5]))) * self.pLow

        # return decoded values
        return(dict(upValue = self.upValue, upUnit = self.upUnit, lowValue = self.lowValue, lowUnit = self.lowUnit))