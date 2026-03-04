import pyvisa

class LakeShoreController:
    def __init__(self, resource_name):
        self.rm = pyvisa.ResourceManager()
        self.instrument = self.rm.open_resource(resource_name)
        self.instrument.timeout = 5000
        self.instrument.write_termination = '\n'
        self.instrument.read_termination = '\n'

    def identify(self):
        return self.instrument.query("*IDN?")

    def read_temperature(self, channel="A"):
        return float(self.instrument.query(f"KRDG? {channel}"))

    def set_setpoint(self, loop=1, temperature=4.2):
        self.instrument.write(f"SETP {loop},{temperature}")

    def read_setpoint(self, loop=1):
        return float(self.instrument.query(f"SETP? {loop}"))

    def close(self):
        self.instrument.close()