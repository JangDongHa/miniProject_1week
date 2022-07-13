import db_connector

db = db_connector.db_connect()


def insertManyByareaXY(listData):  # find users data in users
    db.areaXY.insert_many(listData)


def findareaNoByareaXY(areaNo):
    return list(db.areaXY.find({'areaNo': areaNo}, {'_id': False}))


def findareaXYBylatlon(lat, lon):  # if many result data then return only one data
    try:
        return list(db.areaXY.find({'lat': lat, 'lon': lon}, {'_id': False}))[0]
    except:
        return list(db.areaXY.find({'lat': lat, 'lon': lon}, {'_id': False}))

def findareaXYBygudong(gu, dong):  # if many result data then return only one data
    returnlist = []
    try:
        returnlist = list(db.areaXY.find({'gu': gu, 'dong': dong}, {'_id': False}))[0]
    except:
        pass

    if len(returnlist) == 0:
        try:
            return list(db.areaXY.find({'gu': gu}, {'_id': False}))[0]
        except:
            pass

    if len(returnlist) == 0:
        try:
            return list(db.areaXY.find({'gu': gu+dong}, {'_id': False}))[0]
        except:
            return list(db.areaXY.find({'gu': gu+dong}, {'_id': False}))

    fail = {}
    return fail