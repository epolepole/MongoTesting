from bottle import route, run, template
from pymongo import MongoClient
import pymongo



@route('/read_from_mongo/<collection>')
def read_mongo(collection):
    connection = MongoClient('localhost', 27017)
    db = connection.test_database
    col = db[collection]
    item = col.find_one()
    return template('<b>Found this:</b> {{item}}', item=str(item))


@route('/hello/<name>')
def index(name):
    return template('<b>Helo {{name}}</b>!', name=name)


run(host='localhost', port=8080)
