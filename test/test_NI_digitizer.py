import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(
        rate=100000,
        sample_mode=AcquisitionType.CONTINUOUS
    )

    data = task.read(number_of_samples_per_channel=1000)
    print(data)