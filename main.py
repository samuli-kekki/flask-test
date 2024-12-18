from app import create_app
import logging

app = create_app()

app.logger.setLevel(logging.INFO)
app.logger.info("Hello from main.py")

# TODO: comment out for production?
if __name__ == '__main__':
    app.run(debug=True, port=8000)
