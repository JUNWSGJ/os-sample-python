from flask import Flask, jsonify
import os
from pymongo import MongoClient
application = Flask(__name__)

@application.route("/")
def hello():
    return jsonify({'msg': 'success'})

@application.route("/mongo/search")
def test_mongo():
    client = MongoClient('mongodb://goomoo:goomoo32asdyN8h@mongodb/gm')
    db = client.goomoo
    count = db.users.find().count()
    print('count:', count)
    return 'count:{0}\n'.format(count)

@application.route("/mongo/add")
def test_mongo_add():
    client = MongoClient('mongodb://goomoo:goomoo32asdyN8h@mongodb/gm')
    db = client.goomoo
    users = db.users
    users.insert_one({'name':'张三', 'age':18})
    return "succcess!"


@application.route("/env")
def get_env():
    return "FLASK_ENV:" + os.getenv('FLASK_ENV') + "\n"

if __name__ == "__main__":
    application.run()
