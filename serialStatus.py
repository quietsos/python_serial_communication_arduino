import serial

serialPortName = input('\n Enter the port name: ')
serialPortName = '/dev/'+ serialPortName


serialPortObj = serial.Serial(serialPortName) 

print('\n Status: ', serialPortObj)


serialPortObj.close()

print(f'\n Serial port {serialPortName} closed \n')

   
    
