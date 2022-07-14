import pandas as pd

from model import areaXYDao


class read_csv_for_areaNo:
    def __init__(self, file_name="C:\\Users\\jdh33\\OneDrive\\Desktop\\SpartaCoding\\apiDocs\\지역별-지점코드_20220103_.csv"): # 나중에 상대경로로 바꾸기
        df = self.configuration(file_name)
        self.set_all_data_in_df(df)
        self.list = self.make_json_list(len(df))

    def configuration(self, file_name):
        file_name = file_name
        df = pd.read_csv(file_name, encoding='cp949')
        return df

    def get_oneData_in_all(self, all, i):
        return all.get(i)

    def set_all_data_in_df(self, df):
        self.areaNo_all = df.head(len(df)).to_dict().get('행정구역코드')  # 3787
        self.si_all = df.head(len(df)).to_dict().get('1단계')
        self.gu_all = df.head(len(df)).to_dict().get('2단계')
        self.dong_all = df.head(len(df)).to_dict().get('3단계')  # 없으면 none
        self.x_all = df.head(len(df)).to_dict().get('격자 X')
        self.y_all = df.head(len(df)).to_dict().get('격자 Y')
        self.lat = df.head(len(df)).to_dict().get('위도(초/100)')
        self.lon = df.head(len(df)).to_dict().get('경도(초/100)')

    def make_json_list(self, df_len):
        list = []
        for i in range(0, df_len):
            json_form = {
                'areaNo': self.get_oneData_in_all(self.areaNo_all, i),
                'si': self.get_oneData_in_all(self.si_all, i),
                'gu': self.get_oneData_in_all(self.gu_all, i),
                'dong': self.get_oneData_in_all(self.dong_all, i),
                'x': self.get_oneData_in_all(self.x_all, i),
                'y': self.get_oneData_in_all(self.y_all, i),
                'lat': self.get_oneData_in_all(self.lat, i),
                'lon': self.get_oneData_in_all(self.lon, i)
            }
            list.append(json_form)
        return list

    def getList(self):
        return self.list

# if __name__ == '__main__': # csv data 를 db 에 넣는 것. 절대 실행하지 말 것!! (Warning! don't execute)
#      csv_data_json_list = read_csv_for_areaNo().getList()
#      areaXYDao.insertManyByareaXY(csv_data_json_list)
