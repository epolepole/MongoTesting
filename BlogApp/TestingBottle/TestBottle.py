from bottle import route, post, run, template, debug, request
import bottle
from pymongo import MongoClient


@route('/')
def home_page():
    mythings = ['apple', 'banana', 'pineapple']
    return template('hello_world', username="Lope", things=mythings)
    # return "Hello World\n"


@post('/favourite_fruit')
def favourite_fruit():
    fruit = request.forms.get("fruit")
    if not fruit or fruit == "":
        fruit = "No Fruit Selected"
    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")


@route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")
    return template('fruit_selection.tpl', {'fruit': fruit})


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
