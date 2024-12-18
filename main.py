""" Main entry point of the measurement emitter server. """

from app import create_app
from app.persist import start_persisting
import logging

app = create_app()
app.logger.setLevel(logging.INFO)

# Start reading temperatures and storing to database.
# Starting the thread here seems to be best place.
# Pass app as it would be awkward to import it.
start_persisting(app)

if __name__ == '__main__':
    app.logger.info("Main function running")
    # If debug=True, it starts the app second time,
    # and we have two background threads storing data to database.
    app.run(debug=False, port=8000)
