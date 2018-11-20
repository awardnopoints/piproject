from __future__ import division
from collections import Counter
import serial, time, datetime, sys
from time import sleep
from xbee import XBee
from firebase import firebase

def write_to_database(current):
    firebase = firebase.FirebaseApplication('https://okupyd.firebaseio.com/', None)
    seats = 'seats'
    buildingID = "ChIJSXFbmjAJZ0gRtYltUXsp3YA"
    roomID = 'A'
    seatID = '1'
    result = firebase.put(seats+'/'+buildingID+'/'+roomID+'/'+seatID,"occupied", 0)

"""
def temp_convert(voltage):
    if isinstance(voltage, (int, long)):
        voltage = voltage * (5000.0/1024.0)
        celsius = (voltage - 500) / 10
        return celsius
"""

def get_voltage():
    response = xbee.wait_read_frame()
    voltage = respons['samples'][0]['adc-0']
    return voltage

SERIALPORT = "/dev/ttyUSB0"
BAUDRATE = 9600

ser = serial.Serial(SERIALPORT, BAUDRATE)

xbee = XBee(ser)

print ('Starting Up Temperature Monitor')

i = 0
base_temp_list = []
while i < 10 : # first 10 values
    #response = xbee.wait_read_frame()       
    voltage = get_voltage()
    print(voltage)
    base_temp_list.append(voltage)
    i += 1
data = Counter(base_temp_list) # countes the occurence of each value in the list
base_temp = data.most_common(1) # the mode of the list
print("Base temp is", base_temp)
human_presence = base_temp[0][0] + (base_temp[0][0] * 0.02) # 2% increase in temperature
print("Human presence threshold", human_presence)

while True:
    try:
        temp_file = open('temp_data.xls', 'a')
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #response = xbee.wait_read_frame()       
        voltage = getvoltage()
        if voltage >= human_presence:
            print("Base temp is", base_temp)
            print("Human presence detected", voltage)
            temp_file.write("{}, {}, yes\n".format(timestamp, voltage))
        else:
            print("Base temp is", base_temp)
            print("Chair empty", voltage)
            temp_file.write("{}, {}, no\n".format(timestamp, voltage))
        temp_file.close()
        sleep(1)
        
    except KeyboardInterrupt:
        break

ser.close()
