from workers import DataProvider, DataHandler
from global_variables import cities_aqi
import time

# api in use: https://aqicn.org/api/

if __name__ == '__main__':
    data_provider = DataProvider()
    data_handler = DataHandler()

    if not data_provider.test_conn():
        print('Api endpoint not available')
    else:
        data_provider.start()
        data_handler.start()
        for i in range(100):
            print(cities_aqi)
            time.sleep(0.5)

        data_provider.stop()
        data_handler.stop()
