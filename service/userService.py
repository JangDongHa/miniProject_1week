from model import usersDao


def getUsersData():  # call DAO 잡일 + 모델(CRUD) 요청
    result = usersDao.findUsersByUsers() # list
    return result

