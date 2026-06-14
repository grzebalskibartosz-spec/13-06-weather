import pandas as pd
import openpyxl
import os

from config import Config

flights = [
    {
        "flight_number": "LO123",
        "from": "Warszawa",
        "to": "Londyn",
        "price": 850,
        "duration": 150,
        "airline": "LOT"
    },
    {
        "flight_number": "FR456",
        "from": "Kraków",
        "to": "Rzym",
        "price": 320,
        "duration": 120,
        "airline": "Ryanair"
    },
    {
        "flight_number": "W678",
        "from": "Gdańsk",
        "to": "Oslo",
        "price": 450,
        "duration": 105,
        "airline": "Wizz Air"
    },
    {
        "flight_number": "LH789",
        "from": "Warszawa",
        "to": "Berlin",
        "price": 500,
        "duration": 80,
        "airline": "Lufthansa"
    },
    {
        "flight_number": "BA321",
        "from": "Poznań",
        "to": "Londyn",
        "price": 950,
        "duration": 140,
        "airline": "British Airways"
    },
    {
        "flight_number": "AF654",
        "from": "Warszawa",
        "to": "Paryż",
        "price": 780,
        "duration": 135,
        "airline": "Air France"
    },
    {
        "flight_number": "KL852",
        "from": "Wrocław",
        "to": "Amsterdam",
        "price": 620,
        "duration": 110,
        "airline": "KLM"
    },
    {
        "flight_number": "TK963",
        "from": "Warszawa",
        "to": "Stambuł",
        "price": 1200,
        "duration": 180,
        "airline": "Turkish Airlines"
    },
    {
        "flight_number": "SN741",
        "from": "Katowice",
        "to": "Bruksela",
        "price": 540,
        "duration": 115,
        "airline": "Brussels Airlines"
    },
    {
        "flight_number": "IB258",
        "from": "Warszawa",
        "to": "Madryt",
        "price": 980,
        "duration": 220,
        "airline": "Iberia"
    }
]
countries = {
    "names": ["Polska","Niemcy","Japonia"],
    "capitals": ["Warszawa","Berlin","Tokio"]
}

#df = pd.DataFrame(flights)
# print(df)
# print(df['from'])
# df.to_csv('test.csv', index=False)
# df.to_excel('test2.xlsx', index=False)
#df_v3 = pd.read_excel('test2.xlsx')
#print(df_v3)

import pandas as pd
from config import Config
import os

def save_file(data):
    new_df = pd.DataFrame(data)
    try:
        if os.path.exists(Config.WEATHER_FILE):
            old_df = pd.read_excel(Config.WEATHER_FILE)
            df = pd.concat([old_df, new_df], ignore_index=True)
            df.to_excel(Config.WEATHER_FILE, index=False)
        else:
            new_df.to_excel(Config.WEATHER_FILE, index=False)
    except Exception as e:
        print(e)


        def read_file():
            try:
                df = pd.read_excel(Config.WEATHER_FILE)
                return df
            except:
                print('Wystąpił błąd')