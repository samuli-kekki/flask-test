from .sensor import Sensor
from .measurement import Measurement

import math
import time
from datetime import datetime

class Temperature(Sensor):
    """ Temperature, instance of Sensor """

    def value(self) -> Measurement:
        """ Get sensor reading as Measurement
            Returns: Measurement """
        seconds = time.time() # This returns seconds since epoch
        angle = (seconds % 60) / 60 # Scale every minute to values 0-1
        angle = angle * math.pi * 2 # One phase of sine in one minute
        value = 20 + math.sin(angle) * 5 # Temp will be 20 +- 5
        timestamp = datetime.now().isoformat()
        return Measurement(value, timestamp)

    def unit(self) -> str:
        """ The unit of the measurement """
        return "Celcius"

    def name(self) -> str:
        """ Name/category of measurement """
        return "Temperature"    
