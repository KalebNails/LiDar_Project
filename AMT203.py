#!/usr/bin/python3

"""
Released under MIT License


Copyright (c) 2019 CMU-TBD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from pyftdi.spi import (
    SpiController
)

class AMT203():

    def __init__(self):
         # Instanciate a SPI controller
        print("initalising")
        spi = SpiController()
        spi.configure('ftdi://::/1')
        # The sensor AMT203-V is the slave
        # https://www.cui.com/product/resource/amt20.pdf
        self.slave = spi.get_port(cs=0, freq=spi.frequency/32, mode=0)

    def send_command(self, command_in_hex):
        out = self.slave.exchange([command_in_hex], readlen=1, duplex=True)
        return bytes(out).hex()

    def read_angle(self):
        rtrn = self.send_command(0x10)
        while rtrn != "10":
            rtrn = self.send_command(0x00)
        msb = self.send_command(0x10)
        lsb = self.send_command(0x10)
        angle_in_hex_string = msb + lsb
        return int(angle_in_hex_string, 16)

    def set_zero_point(self):
        rtrn = self.send_command(0x70)
        while rtrn != "80":
            rtrn = self.send_command(0x00)
            
print("testing")
sensor = AMT203()
#print(sensor.read_angle)
