from flask import Blueprint, Response, request, jsonify
from .sensors.measurement_manager import MeasurementManager
from .sensors.temperature_sensor import Temperature
from .database_models import PersistedMeasurement
from .sensors.measurement import Measurement

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

@measurement_blueprint.route('/temperature', methods=['GET'])
def get_temperatures():
    """ Return N most recent readings from the database """

    num_readings = request.args.get("limit", type=int)
    # Get only temperature results (although we only have temperatures for now)
    # Sort by timestamp descending, most recents first
    db_query = PersistedMeasurement.query.filter_by(name='Temperature').order_by(PersistedMeasurement.timestamp.desc())

    # Limit results?
    if num_readings:
        db_results = db_query.limit(num_readings).all()
    else:
        db_results = db_query.all()

    # Gether results in a list
    results = []
    for db_result in db_results:
        # Create Measurement instance - although we could maybe just read the values in a dict.
        measurement = Measurement(db_result.value, db_result.timestamp.isoformat())
        # Convert to plain dict so that we can easily return JSON soon.
        results.append(measurement.__dict__)
    
    return jsonify(results)
