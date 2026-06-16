import time

import pyvisa
import minimalmodbus
import serial
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY, GaugeMetricFamily
from prometheus_client.registry import Collector

class DewPointCollector(Collector):
    def __init__(self):
        self._ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
        # self._ser.open()
        self._myVaisala = minimalmodbus.Instrument(
            self._ser, 33, minimalmodbus.MODE_RTU, True, False
        )

    def collect(self):
        c = GaugeMetricFamily(
            "coldbox_dewpoint", "Dewpoint within the coldbox (milli-Kelvin)", labels=["sensor"]
        )
        data = self._myVaisala.read_registers(0, 4, 4)
        c.add_metric(["top"], data[1])
        c.add_metric(["bottom"], data[3])
        yield c

class ChillerCollector(Collector):
    def __init__(self):
        self._resource = pyvisa.ResourceManager().open_resource("TCPIP::10.116.2X.XX::5050::SOCKET")
        self._resource.write_termination = '\r'
        self._resource.read_termination = '\r'

    def collect(self):
        c = GaugeMetricFamily(
            "coldbox_chiller", "Chiller for the coldbox"
        )
        c.add_metric(["temperature"], self._resource.query("in_pv_00"))
        yield c


REGISTRY.register(DewPointCollector())
# REGISTRY.register(ChillerCollector())

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(9090)

    import time

    while True:
        time.sleep(1)
