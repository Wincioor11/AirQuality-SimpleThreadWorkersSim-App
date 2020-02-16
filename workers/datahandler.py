from .worker import Worker
import time
from global_variables import cities_aqi


class DataHandler(Worker):

    def __init__(self):
        super().__init__()

    def run(self):
        while self.run_flag:
            with self.lock:
                for city in cities_aqi:
                    if cities_aqi[city]['info'] == '':
                        aqi = cities_aqi[city]['aqi']
                        cities_aqi[city]['info'] = self.get_info_from_aqi(aqi)
            time.sleep(2)

    def get_info_from_aqi(self, aqi):
        if 0 <= aqi <= 50:
            return 'Good'
        elif 50 < aqi <= 100:
            return 'Moderate'
        elif 100 < aqi <= 150:
            return 'Unhealthy for Sensitive Groups'
        elif 150 < aqi <= 200:
            return 'Unhealthy'
        elif 200 < aqi <= 300:
            return 'Very Unhealthy'
        elif 300 < aqi:
            return 'Hazardous'








