from model import usersDao


def getUsersData():  # call DAO 잡일 + 모델(CRUD) 요청
    print('2. find users_data for controller in userService (2. userService에서 controller가 요청한 유저데이터를 찾기 시작합니다.)')
    print('3. find users_data to usersDao in userService (3. userService에서 유저데이터를 찾기 위해 userDao를 호출합니다.)')
    result = usersDao.findUsersByUsers() # list
    print('6. caught users_data from usersDao in userService (6. userService 에서 userDao로부터 유저데이터를 받았습니다.)')
    print('7. return users_data to userController in userService (7. 유저데이터를 return 해줍니다.)')
    return result