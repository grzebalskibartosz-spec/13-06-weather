

import time
from services.openweather_api import get_weather
from services.excel_files import save_file

# data_from_file = read_file()
# print(data_from_file)

while True:
    weather_record = get_weather()
    save_file([weather_record])
    print("Pobrano informacje")
    time.sleep(10)