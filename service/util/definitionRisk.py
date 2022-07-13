safelist = ['없음', '맑음']
middleList = ['흐림']
dangerTemp = 25

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
