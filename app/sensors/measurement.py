
class Measurement:
    value: float # Value of the measurement
    timestamp: str # ISO string of measurement date

    def __init__(self, value: float, timestamp: str):
        self.value = value
        self.timestamp = timestamp

    def json(self) -> str:
        return f'{{ "value": {self.value}, "timestamp": {self.timestamp} }}'
