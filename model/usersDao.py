from pymongo import ReturnDocument

import db_connector

db = db_connector.db_connect()

def findUsersByUsers(): # find users data in users
    return list(db.users.find({}, {'_id':False}))

def insertUsers(user):
    try:
        db.users.insert_one(user)
    except:
        print("can't insert user data")

def findEmailByUsers(email):
    try:
        return list(db.users.find({'email': email}, {'_id':False}))[0]
    except:
        return False

def findEmailPasswordByUsers(email, password):
    try:
        return list(db.users.find({'email': email, 'password': password}, {'_id': False}))[0]
    except:
        return False

def findOneAndUpdateByusers(username, password, address):
    return db.users.find_one_and_update({'email': username, 'password': password},
                                              {'$set': {"address": address}})

def findOneAndUpdateAddrByusers(username, address):
    return db.users.find_one_and_update({'email': username},
                                              {'$set': {"address": address}})