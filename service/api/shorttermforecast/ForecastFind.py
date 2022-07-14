from service.api.shorttermforecast.ForecastTypeEnum import ForecastType


class forecastFind:

    def __init__(self, response):
        try:
            self.items = response.get('response').get('body').get('items').get('item')
        except:
            raise Exception(response)

    def category(self, enum):
        list = []
        for item in self.items:
            if enum == item.get('category'):
                self.casting_fcstValue_to_korean(item)
                self.casting_type_to_korean(item)
                list.append(item)
        return list

    def casting_type_to_korean(self, item):
        for fType in list(ForecastType):
            if item['category'] == fType.name:
                item['category'] = fType.value

    def casting_fcstValue_to_korean(self, item):
        if item['category'] == ForecastType.PTY.name:
            item['fcstValue'] = ForecastType.convert_PTY_code(ForecastType, item['fcstValue'])
        elif item['category'] == ForecastType.SKY.name:
            item['fcstValue'] = ForecastType.convert_SKY_code(ForecastType, item['fcstValue'])
