# flask-test

# TODO

- [x] Create requirements.txt file
- [x] Create virtual environment
- [x] Create .gitignore
- [x] Create initial folder structure
- [x] Create app main file
- [x] Create docker-compose and Docker files
- [x] Add gunicorn
- [x] Test with dummy GET API
- [x] Create SQLAlchemy model class for measurements, create tables
- [x] Implement measurement class
- [x] Implement manager that throttles measurements and implements a generator
- [x] Create a streaming GET API and return temperatures as SSE now (Server-Sent Events)
- [x] Create a thread that stores temperatures to database
- [x] Create GET API that returns N latest values from the database
- [ ] Test that it works in Docker too
- [ ] Document code
- [ ] Unit and integration tests
- [ ] Generate API documentation (investigate Flasgger, Flask-RESTPlus, Flask-OpenAPI3, APIFairy, etc.)

# Documentation

Use following command to build & start the app and the database:
docker-compose up

Following builds the app:
docker-compose build

This starts only the database if you'd like to test the app on command line:
docker-compose up measurement_postgres

As we are not using -d, you can stop the server with CTRL-C.

The data in the database is not persisted.

# Notes:

Investigate what is a good way to return streaming temperatures. Currently it is returning JSON fragments, not one complete JSON document.

Investiagate adding index for timestamp column in the database schema. How to add indexes with SQLAlchemy?

Investigate using a time series database.

datetime.utcnow is deprecated, investigate alternative

Input validation for the APIs (limit could have a range of acceptable values)

Handle app shut down gracefully in persisting thread

