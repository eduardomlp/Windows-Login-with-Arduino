import win32com.client as OSsender
import sys
import serial
import gc
import time

password = 'YOUR PASSWORD HERE!!!' 

def SendPassword():
    keySender = OSsender.Dispatch("WScript.Shell")
    keySender.SendKeys('{ENTER}')
    keySender.SendKeys(password)
    keySender.SendKeys('{ENTER}')

# Function adapted from: http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
def GetSerialPorts():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            return port
        except (OSError, serial.SerialException):
            pass
        
def MainFunction():
    gc.enable()
    while True:
        arduinoSerial = serial.Serial(GetSerialPorts(), 9600)
        serialRead = arduinoSerial.read(4)

        if serialRead == "True" :
            SendPassword()
            break

        gc.collect()
        time.sleep(2)
        
if __name__ == '__main__':       
    MainFunction()
