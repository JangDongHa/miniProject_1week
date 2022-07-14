from config import dangerTemp, middleList, safelist

def check_risk(data):
    if data in middleList:
        return 'color: #fd7e14;'
    if data in safelist:
        return 'color: green'
    try:
        if int(data) >= dangerTemp:
            return 'color: red'
        else:
            return 'color: green'
    except:
        pass
    return 'color: red'
