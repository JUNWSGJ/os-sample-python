from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/env")
def get_env():
    return "FLASK_ENV:" + os.getenv('FLASK_ENV') + "\n"

if __name__ == "__main__":
    application.run()
