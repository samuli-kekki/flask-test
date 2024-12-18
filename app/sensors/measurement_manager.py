from .sensor import Sensor
from .measurement import Measurement
from typing import Generator
import time

class MeasurementManager:
    """ Mechanism for throtting measurements
    and getting a stream/generator of measurements. """

    def __init__(self, sensor: Sensor, delay: float):
        """ Create MeasurementManager.
        Args:
            sensor (Sensor): Instance of Sensor to read measurements from
            delay (float): Delay between measurement readings"""
        self.sensor = sensor
        self.delay = delay
        self.last_measurement_time = time.time() # Returns seconds since epoch

    def _sleep(self):
        """ Sleep based on self.delay setting """
        elapsed_time = time.time() - self.last_measurement_time
        if elapsed_time < self.delay:
            time.sleep(self.delay - elapsed_time)
        self.last_measurement_time = time.time()

    def get_measurement_iterator(self) -> Generator[Measurement, None, None]:
        """ Return interator for Sensor measurements.
        Returns:
            Generator[Measurement, None, None]: Generator for Sensor measurements """

        while True:
            self._sleep() # Sleep if necessary before the next measurement time
            value = self.sensor.value() # Get a new value
            yield value # Yield it
