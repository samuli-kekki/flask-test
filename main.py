from app import create_app
from app.persist import start_persisting
import logging

app = create_app()
app.logger.setLevel(logging.INFO)

# Start reading temperatures and storing to database.
# Starting the thread here seems to be best place.
# Pass app as it would be awkward to import it.
start_persisting(app)

# TODO: comment out for production?
if __name__ == '__main__':
    app.run(debug=True, port=8000)
