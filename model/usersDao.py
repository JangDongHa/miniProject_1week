import db_connector

def findUsersByUsers(): # find users data in users
    print("4. find users_data to mongodb in usersDao (4. usersDao가 유저데이터를 몽고db에서 찾습니다.)")
    db = db_connector.db_connect()
    print("5. return users_data in usersDao (5. userDao가 유저데이터를 return 해줍니다.)")
    return list(db.users.find({}, {'_id':False}))
