import requests

from service.api.heatshelter import shelterCode

url = 'http://apis.data.go.kr/1741000/HeatWaveShelter2/getHeatWaveShelterList2'
key = 'wFaw7OFBqe4265nYPtDX2VQSJQke95gx56upeVRviZyp2TSZis/KZBM8Sc6fZwq8aF6vzD3HjIB3lzLOJBGYSQ=='


def setting_data(areaCd):
    return {
        'ServiceKey': key,
        'year': 2022,
        'areaCd': areaCd,
        'equptype': '001',
        'type': 'JSON',
        'pageNo': 1,
        'numOfRows': 10
    }


def connection(url, param):
    r = requests.get(url, params=param)
    try:
        return r.json()
    except:
        return r.text()

def change_equptype_to_korean():
    r_list = []
    for equptype in range(1, 10):
        data['equptype'] = '00' + str(equptype)
        r_list.append(connection(url, data))
    data['equptype'] = '010'
    r_list.append(connection(url, data))
    return r_list

def get_all_equptype_data(url, data):
    r_list = change_equptype_to_korean()
    new_r_list = drop_none_result_data(r_list)
    return make_many_to_one_r_list(new_r_list)


def drop_none_result_data(r_list):
    new_r_list = []
    for json in r_list:
        try:
            json['RESULT']
        except:
            new_r_list.append(json['HeatWaveShelter'][1]['row'])
    return new_r_list


def make_many_to_one_r_list(new_r_list):
    length = len(new_r_list)
    if length == 1:
        return new_r_list
    else:
        for index in range(1, length):
            for value in new_r_list[index]:
                new_r_list[0].append(value)
    return new_r_list[0]


def change_json_key_name(shelter_info):
    shelter_info['phoneNumber'] = shelter_info['mngdptCd']
    shelter_info.pop('mngdptCd')

    shelter_info['xcord'] = shelter_info['la']
    shelter_info['ycord'] = shelter_info['lo']
    shelter_info.pop('la')
    shelter_info.pop('lo')


def change_json_value_name(shelter_info, key):
    shelter_info[key] = shelterCode.code(shelter_info[key])


def update_json_i_want(result, *args):  # args : pop 하려는 대상
    for shelter_info in result:
        for arg in args:
            shelter_info.pop(arg)
        change_json_key_name(shelter_info)
        change_json_value_name(shelter_info, 'equptype')

    return result


def get_need_result(result):
    return update_json_i_want(result, 'restSeqNo', 'year', 'creDttm', 'updtDttm', 'areaNm',
                              'operBeginDe', 'operEndDe', 'ar', 'colrHoldElefn', 'colrHoldArcndtn',
                              'chckMatterNightOpnAt',
                              'chckMatterWkendHdayOpnAt', 'chckMatterStayngPsblAt', 'rm', 'dtlAdres',
                              'mngdpt_cd', 'xcord', 'ycord', )


if __name__ == '__main__':
    data = setting_data('4687025000')
    result = get_all_equptype_data(url, data)  # 형태 : list({},{},{}....)
    myData = get_need_result(result)  # 그 중에서 필요한 데이터만 정제한 것
