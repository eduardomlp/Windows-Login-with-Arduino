import serial
import gc
import time
from subprocess import Popen, PIPE

passwordSequence = ''' 
key s
key e
key n
key h
key a
key Return
'''

def SendPassword():
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=passwordSequence)


def MainFunction():
    gc.enable()
    while True:
        arduinoSerial = serial.Serial('/dev/ttyACM0', 9600)
        serialRead = arduinoSerial.read(4)

        if serialRead == "True" :
            SendPassword()
            #osWriter.write("Minha Senha!")
            #break

        gc.collect()
        time.sleep(2)
        
if __name__ == '__main__':       
    MainFunction()


