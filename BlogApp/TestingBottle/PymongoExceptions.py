import pymongo

connection = pymongo.MongoClient('localhost',27017)

db = connection.test_database
users = db.users

doc = {'first': 'Lope', 'lastname': 'Ramos'}
print(str(doc))
print("about to isnert the document")

try:
    users.insert_one(doc)
except Exception as e:
    print("insert failed: " + str(e))

print(str(doc))
print("inserting again")

try:
    users.insert_one(doc)
except Exception as e:
    print("second insert failed: " + str(e))
