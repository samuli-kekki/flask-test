from abc import ABC, abstractmethod
from .measurement import Measurement

class Sensor(ABC):
    """Fictional sensor interface"""

    @abstractmethod
    def value(self) -> Measurement:
        """ Get sensor reading as Measurement
            Returns: Measurement """
        pass

    @abstractmethod
    def unit(self) -> str:
        """ The unit of the measurement, e.g. Celcius """
        pass

    @abstractmethod
    def name(self) -> str:
        """ Name/category of measurement, e.g. Temperature """
        pass
