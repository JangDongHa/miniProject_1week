class ipDTO:
    def __init__(self, json):
        self.status = json['status']
        self.country = json['country']
        self.countryCode = json['countryCode']
        self.region = json['region']
        self.regionName = json['regionName']
        self.city = json['city']
        self.zip = json['zip']
        self.lat = json['lat']
        self.lon = json['lon']
        self.timezone = json['timezone']
        self.isp = json['isp']
        self.org = json['org']
        self.query = json['query']

    def get_lat_lon(self):
        return int(self.lat), int(self.lon)