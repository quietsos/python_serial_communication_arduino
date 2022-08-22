import serial


serialObj = serial.Serial('/dev/ttyACM0',9600)

print('\n Default settings:')
print('PORT         =', serialObj.port)
print('Baudrate     =', serialObj.baudrate)
print('ByteSize     =', serialObj.bytesize)
print('Parity       =', serialObj.parity)
print('StopBits     =', serialObj.stopbits)

serialObj.close()