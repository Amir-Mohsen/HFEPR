import serial
import time

class ANC300:
    def __init__(self, port, baudrate=38400):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)

    def send(self, command):
        cmd = command + "\r\n"
        self.ser.write(cmd.encode())
        return self.ser.readline().decode().strip()

    def select_axis(self, axis):
        return self.send(f"AXIS {axis}")

    def set_frequency(self, freq):
        return self.send(f"FREQ {freq}")

    def set_voltage(self, voltage):
        return self.send(f"VOLT {voltage}")

    def step(self, steps):
        return self.send(f"STEP {steps}")

    def close(self):
        self.ser.close()