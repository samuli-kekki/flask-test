from flask import Blueprint, Response
from .sensors.measurement_manager import MeasurementManager
from .sensors.temperature_sensor import Temperature

# Create a blueprint for better managing the routes
measurement_blueprint = Blueprint('measurement', __name__, url_prefix='/measurement')

@measurement_blueprint.route('/temperature/stream', methods=['GET'])
def get_temperature_stream():

    # Stream content with a generator function, i.e. Server-Sent Events:
    # https://flask.palletsprojects.com/en/stable/patterns/streaming/
    def event_stream():
        # Stream temperature once per second.
        manager = MeasurementManager(Temperature(), 1.0)
        # This iterator should give us a new value once per second or so.
        stream = manager.get_measurement_iterator()
        # Note: How this is implemented, it does not return fully qualified
        # JSON document. Instead, it returns a stream of partial JSON.
        # TODO: investigate if this is a good idea.
        while True:
            yield next(stream).json()

    return Response(event_stream(), content_type='text/event-stream')
