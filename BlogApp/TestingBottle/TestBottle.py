from bottle import route, run, template, debug
from pymongo import MongoClient
import pymongo


@route('/')
def home_page():
    mythings = ['apple', 'banana', 'pineapple']
    return template('hello_world', username="Lope", things=mythings)
    # return "Hello World\n"


@route('/testpage')
def test_page():
    return "This is a test page"


@route('/read_from_mongo/<collection>')
def read_mongo(collection='names'):
    connection = MongoClient('localhost', 27017)
    db = connection.test_database
    col = db[collection]
    item = col.find_one()
    return template('<b>Hello mister {{item}}</b>', item=str(item['name']))


@route('/hello/<name>')
def hello(name):
    return template('<b>Helo {{name}}</b>!', name=name)


debug(True)
run(host='localhost', port=8080)
