import serial
from xbee import XBee
def get_voltage():
    response = xbee.wait_read_frame()
    voltage = response['samples'][0]['adc-0']
    return voltage

SERIALPORT = "/dev/ttyUSB0"
BAUDRATE = 9600

ser = serial.Serial(SERIALPORT, BAUDRATE)

xbee = XBee(ser)
