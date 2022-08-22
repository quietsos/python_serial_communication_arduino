import serial
import time

serialObj = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(3)

serialObj.timeout = 30
receiveString = serialObj.readline()

print(receiveString)

serialObj.close()
