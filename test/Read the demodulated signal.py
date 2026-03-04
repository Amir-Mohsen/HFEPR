import zhinst.core
import time

daq = zhinst.core.ziDAQServer('localhost', 8004, 6)
device = 'devXXXX'

path = f'/{device}/demods/0/sample'

daq.subscribe(path)

daq.sync()

print("Reading data...")

for i in range(10):
    data = daq.poll(0.1, 500, 0, True)

    if path in data:
        sample = data[path]
        x = sample['x'][-1]
        y = sample['y'][-1]
        r = (x ** 2 + y ** 2) ** 0.5

        print(f"X: {x:.6f}, Y: {y:.6f}, R: {r:.6f}")

    time.sleep(0.2)

daq.unsubscribe(path)