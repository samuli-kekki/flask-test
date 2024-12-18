from flask import Flask

def create_app():
    app = Flask(__name__)

    # Testing ... TODO remove later
    @app.route('/', methods=['GET'])
    def test_handler():
        return "hi"
        
    return app
