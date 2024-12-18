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
- [ ] Create SQLAlchemy model class for measurements, create tables
- [x] Implement measurement class
- [x] Implement manager that throttles measurements and implements a generator
- [ ] Create a streaming GET API and return temperatures as SSE now (Server-Sent Events)
- [ ] Create a thread that stores temperatures to database
- [ ] Create GET API that returns N latest values from the database
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
