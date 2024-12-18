
from .sensors.temperature_sensor import Temperature
from .sensors.measurement_manager import MeasurementManager
from .database_models import PersistedMeasurement
from . import db
from threading import Thread

def persist_temperatures(app):
    # Need to push app context to be able to use the db.
    with app.app_context():
        sensor = Temperature()
        manager = MeasurementManager(sensor, 2.0) # Save to db every 2s
        stream = manager.get_measurement_iterator()
        
        # TODO handle app shut down and break from the loop
        while True:
            measurement = next(stream) # Measurement instance
            persisted_measurement = PersistedMeasurement(
                value = measurement.value,
                timestamp = measurement.timestamp,
                name = sensor.name(),
                unit = sensor.unit()
            )

            db.session.add(persisted_measurement)
            db.session.commit()
            app.logger.info("Persisted temperature")

def start_persisting(app):
    """ Starts a background thread """
    t = Thread(target=persist_temperatures, args=(app, ))
    t.daemon = True # Stop automatically at app shut down
    t.start()
