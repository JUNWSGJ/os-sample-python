from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!" + os.getenv('FLASK_ENV')

if __name__ == "__main__":
    application.run()
