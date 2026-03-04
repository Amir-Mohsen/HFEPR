import zhinst.core

# Connect to Data Server (default local)
daq = zhinst.core.ziDAQServer('localhost', 8004, 6)

# Replace with your device ID (e.g., 'dev1234')
device = 'devXXXX'

print(daq.getString(f'/{device}/features/devtype'))