from datetime import datetime, timedelta

from model import areaXYDao


class formatConvertor:
    def __init__(self, data=None):
        try:
            self.data = data.get('response').get('body').get('items').get('item')[0]
        except AttributeError:
            print('Error in formatConvertor because Response data is none')
            self.data = data

    def setData(self, data):
        try:
            self.data = data.get('response').get('body').get('items').get('item')[0]
        except:
            self.data = data

    def convert_h(self, data, key):
        try:
            addTime = int(key.split('h')[1])  # split h1
        except:
            print('key format Error in formatConvertor')
        dataDatetime = self.date_to_datetime(data.get('date'))
        dataDatetime = self.datetime_add_hHours(dataDatetime, addTime)

        newKey = self.datetime_to_string(dataDatetime)
        data[newKey] = data.get(key)
        data.pop(key)

    def execute(self):
        for i in range(1, 79):  # h1 ~ h78
            self.convert_h(self.data, 'h' + str(i))
        return self.data

    def date_to_datetime(self, date):
        year, month, day, hour = self.datetime_format(date)

        return datetime(year=year, month=month, day=day, hour=hour)

    def datetime_format(self, date):  # date : 2022070818
        year = int(date[0:4])
        if date[4] == '0':
            month = int(date[5:6])
        else:
            month = int(date[4:6])
        if date[6] == '0':
            day = int(date[7:8])
        else:
            day = int(date[6:8])
        if date[8] == '0':
            hour = int(date[9:])
        else:
            hour = int(date[8:])

        return year, month, day, hour

    def datetime_add_hHours(self, datetime, hours):
        return datetime + timedelta(hours=hours)


    def datetime_to_string(self, datetime):
        year = datetime.strftime('%Y')
        month = datetime.strftime('%m')
        day = datetime.strftime('%d')
        time = datetime.strftime('%H')
        return year + month + day + time

    def data_to_custom_predict_data(self, untilTime):  # untilTime : 에를들어 기본 date가 202201012200 이면 여기서부터 예측값 6시간후까지 뽑으려면 untilTime=6
        default_len = 3
        keys = list(self.data.keys())  # 3 = h1 ~ (길이 3부터 h1 ~)
        values = list(self.data.values())
        newData = dict()
        for i in range(0, default_len + untilTime):
            newData[keys[i]] = values[i]
        return newData

    def get_predict_list_data(self, number, dateStr):
        dateTime = self.date_to_datetime(dateStr)
        list_data = []
        for i in range(0,number):
            dateTime = self.datetime_add_hHours(dateTime, 1)
            dateStr = self.datetime_to_string(dateTime)
            temp = self.data.get(dateStr) # 온도
            list_data.append()

        return list_data



if __name__ == '__main__':
    data = {
        "code": "A41",
        "areaNo": "1100000000",
        "date": "2022071118",
        "h1": "29",
        "h2": "29",
        "h3": "29",
        "h4": "30",
        "h5": "28",
        "h6": "28",
        "h7": "28",
        "h8": "27",
        "h9": "27",
        "h10": "27",
        "h11": "27",
        "h12": "26",
        "h13": "27",
        "h14": "27",
        "h15": "28",
        "h16": "29",
        "h17": "29",
        "h18": "30",
        "h19": "31",
        "h20": "31",
        "h21": "32",
        "h22": "32",
        "h23": "32",
        "h24": "32",
        "h25": "31",
        "h26": "30",
        "h27": "30",
        "h28": "29",
        "h29": "28",
        "h30": "28",
        "h31": "28",
        "h32": "28",
        "h33": "28",
        "h34": "27",
        "h35": "27",
        "h36": "26",
        "h37": "26",
        "h38": "26",
        "h39": "26",
        "h40": "26",
        "h41": "27",
        "h42": "28",
        "h43": "28",
        "h44": "27",
        "h45": "28",
        "h46": "28",
        "h47": "28",
        "h48": "29",
        "h49": "29",
        "h50": "29",
        "h51": "29",
        "h52": "28",
        "h53": "28",
        "h54": "28",
        "h55": "28",
        "h56": "28",
        "h57": "28",
        "h58": "27",
        "h59": "27",
        "h60": "27",
        "h61": "27",
        "h62": "27",
        "h63": "28",
        "h64": "28",
        "h65": "28",
        "h66": "28",
        "h67": "29",
        "h68": "31",
        "h69": "31",
        "h70": "31",
        "h71": "30",
        "h72": "30",
        "h73": "29",
        "h74": "28",
        "h75": "27",
        "h76": "27",
        "h77": "27",
        "h78": "28"
    }
    convertor = formatConvertor(data)
    a = convertor.execute()
    print(convertor.data_to_custom_predict_data(6))
