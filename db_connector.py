from pymongo import MongoClient

BASE_URL = "mongodb+srv://test:sparta@cluster0.noj5q89.mongodb.net/Cluster0?retryWrites=true&w=majority"


def db_connect():
    client = MongoClient(BASE_URL)
    db = client.dbsparta

    return db
