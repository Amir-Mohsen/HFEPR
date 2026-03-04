from hardware.anc300 import ANC300
import time

controller = ANC300("COM3")

controller.select_axis(1)
controller.set_frequency(1000)
controller.set_voltage(30)

print("Moving forward 100 steps")
controller.step(100)

time.sleep(1)

print("Moving backward 100 steps")
controller.step(-100)

controller.close()