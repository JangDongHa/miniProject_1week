import db_connector

db = db_connector.db_connect()

def findUsersByUsers(): # find users data in users
    return list(db.users.find({}, {'_id':False}))
