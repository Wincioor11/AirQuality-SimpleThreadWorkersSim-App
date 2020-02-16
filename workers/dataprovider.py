from .worker import Worker
import time
import requests
import random
from global_variables import cities_aqi, city_names


class DataProvider(Worker):

    def __init__(self):
        super().__init__()
        self.token = '7a3b560e5cf5830b4ab1da3f8a4f6309e59ddd36'
        self.endpoint = 'https://api.waqi.info/feed/{city}/?token={token}'

    def run(self):
        while self.run_flag:
            with self.lock:
                city = self.get_random_city()
                aqi = self.get_aqi(city)
                if aqi:
                    if city not in cities_aqi:
                        cities_aqi[city] = {'aqi': aqi, 'info': ''}
                    else:
                        if cities_aqi[city]['aqi'] != aqi:
                            cities_aqi[city] = {'aqi': aqi, 'info': ''}
                        else:
                            continue
            time.sleep(1)

    def test_conn(self):
        response = requests.get(self.endpoint.format(city='demo', token='demo'))
        if response.status_code == 200:
            return True
        else:
            return False

    def get_json(self, city):
        return requests.get(self.endpoint.format(city=city, token=self.token)).json()

    def get_aqi(self, city):
        response = self.get_json(city)
        if response['status'] == 'ok':
            return response["data"]["aqi"]
        else:
            return None

    def get_random_city(self):
        return city_names[random.randrange(len(city_names))]



