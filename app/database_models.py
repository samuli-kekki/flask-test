from . import db
from datetime import datetime

# When we call db.create_all(),
# SQLAlchemy will create a new table called measurements with this schema.

class PersistedMeasurement(db.Model):
    """ This is extended from SQLAlchemy class. """

    __tablename__ = 'measurements' # The name of the table in our database

    # Auto-incrementing primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Value of the measurement
    value = db.Column(db.Float, nullable=False)
    # Timestamp of the measurement. It is using Postgres datatime type here,
    # alghough our code is using strings mostly.
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Timestamp field
    # Unit of the measurement, e.g. "Celcius"
    unit = db.Column(db.String(20), nullable=False)
    # Name of the measurement, e.g. "Temperature"
    name = db.Column(db.String(50), nullable=False)
