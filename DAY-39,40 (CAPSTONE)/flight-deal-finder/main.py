# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from datetime import datetime, timedelta

import flight_search
from flight_search import FlightSearch
from data_manager import DataManager

ORIGIN_CITY_IATA = "LON"
flight_search = FlightSearch()
dm = DataManager()
sheet_data = dm.get_data()
# print(sheet_data)

city_data = []
for i in range(0, len(sheet_data)):
    city_data.append(sheet_data[i]['city'])

dm.put_data(FlightSearch.update(sheet_data, city_data))

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
