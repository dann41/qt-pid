import sys
import glob
import serial
import asyncio

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*[0-9]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port, 9600, timeout=1)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class SerialDevice:
    def __init__(self):
        self.started = False
        
    def start(self, port: str, baudrate: int, callback):
        if (self.started):
            return
        self.started = True

        self.ser = serial.Serial(port = port, baudrate = baudrate, timeout=5)

        self.loop = asyncio.get_event_loop()
        self.loop.add_reader(self.ser, lambda: self.__reader(callback))

    def stop(self):
        self.started = False
        self.ser.close()

    def isStarted(self) -> bool:
        return self.started

    def __reader(self, callback):
        line = ""
        msg = self.ser.read().decode()
        while (msg != '\n'):
            line += msg
            msg = self.ser.read().decode()
        callback(line)

    def send_pir(self, kp: float, ki: float, kd: float):
        message = bytes(f"{kp},{ki},{kd}", 'UTF-8')
        self.loop.call_soon(self.ser.write, message)

