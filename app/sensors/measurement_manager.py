from .sensor import Sensor
from .measurement import Measurement
from typing import Generator
import time

class MeasurementManager:
    """ Mechanism for throtting measurements
    and getting a stream/generator of measurements. """

    def __init__(self, sensor: Sensor, delay: float):
        """ Delay: gap between measurements in seconds.
        The generator will sleep this amount (or less)."""
        self.sensor = sensor
        self.delay = delay
        self.last_measurement_time = time.time() # Returns seconds since epoch

    def sleep(self):
        elapsed_time = time.time() - self.last_measurement_time
        if elapsed_time < self.delay:
            time.sleep(self.delay - elapsed_time)
        self.last_measurement_time = time.time()

    def get_measurement_iterator(self) -> Generator[Measurement, None, None]:
        while True:
            self.sleep() # Sleep if necessary before the next measurement time
            value = self.sensor.value() # Get a new value
            yield value # Yield it
