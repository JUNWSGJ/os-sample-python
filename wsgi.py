import pymysql as pymysql
import redis
from flask import Flask, jsonify
import os
from pymongo import MongoClient
application = Flask(__name__)

@application.route("/")
def hello():
    return jsonify({'msg': 'success'})

@application.route("/mongo/search")
def test_mongo():
    client = MongoClient('mongodb://goomoo:passwd@mongodb/goomoo')
    count = client.goomoo.students.find().count()
    print('count:', count)
    return 'count:{0}\n'.format(count)

@application.route("/mongo/add")
def test_mongo_add():
    client = MongoClient('mongodb://goomoo:passwd@mongodb/goomoo')
    client.goomoo.students.insert_one({'name':'张三', 'age':18})
    return "succcess!"

@application.route("/redis")
def test_redis():
    r = redis.StrictRedis(host='redis', port=6379, db=0 , password='asdu98de3Bdeedsaasodjw342s')
    r.set('foo', 'boo')
    r.get('foo')
    REDIS_URL = "redis://:asdu98de3Bdeedsaasodjw342s@redis:6379/0"
    return r.get('foo')

@application.route("/mysql")
def test_mysql():
    conn = pymysql.connect(host='mysql-57-centos7-ext', port=3306, user='root', passwd='Goomoo!12e3j7we', db='mysql')
    cur = conn.cursor()
    cur.execute("SELECT Host,User FROM user")
    print(cur.description)
    for row in cur:
        print(row)
    cur.close()
    conn.close()
    return 'success'



@application.route("/env")
def get_env():
    return "FLASK_ENV:" + os.getenv('FLASK_ENV') + "\n"

if __name__ == "__main__":
    application.run()
