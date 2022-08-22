import serial
import time


serialObj = serial.Serial('/dev/ttyACM0',9600)

serialObj.baudrate = 9600
serialObj.bytesize = 8
serialObj.parity   = 'N'
serialObj.stopbits = 1

time.sleep(3)



print("Control the lights: ")

print("Enter A for on: \nEnter B for off:")

while True:
    
    command = input("Enter the command: ")

    if command == "A":
        bytesWritten = serialObj.write(b'A')
        print('Byte Written: ', bytesWritten)
        


    elif command == "B":
        bytesWritten = serialObj.write(b'B')
        print('Byte Written: ', bytesWritten)
        


# print("Command for light on: ")
# o = str(input())
# onCommand = serialObj.write(b'o')
# print("Light on status: ", onCommand)

# print("Command for light off: ")
# f = str(input())
# offCommand = serialObj.write(b'f')
# print("Light off status: ", offCommand)



