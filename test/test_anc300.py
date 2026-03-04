import serial
import time

ser = serial.Serial(
    port='COM3',      # change this!
    baudrate=38400,   # common default for ANC300
    timeout=1
)

time.sleep(2)  # give connection time

ser.write(b'VER?\n')
response = ser.readline()
print("Controller response:", response.decode())

ser.close()