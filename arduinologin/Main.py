import serial
import gc
import time
from subprocess import Popen, PIPE

passwordSequence = ''' 
key Return 
key p
key a
key s
key s
key w
key o
key r
key d
key Return
'''

def SendPassword():
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=passwordSequence)


def MainFunction():
    gc.enable()
    while True:
        arduinoSerial = serial.Serial('/dev/ttyACM0', 9600) #/dev/ttyACM0 is the port where arduino is connected
        serialRead = arduinoSerial.read(4)

        if serialRead == "True" :
            SendPassword()
            break

        gc.collect()
        time.sleep(2)
        
if __name__ == '__main__':       
    MainFunction()


