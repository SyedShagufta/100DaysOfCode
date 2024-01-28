import requests
from requests.auth import HTTPBasicAuth
SHEETY_ENDPOINT = "https://api.sheety.co/ceab2dee5bf4d021066960cf2afcacd3/flightDeals/prices"
BASIC = HTTPBasicAuth('sofia', 'Sofia26')

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = None
        self.response = requests.get(url=SHEETY_ENDPOINT, auth=BASIC)

    def get_data(self):
        self.data = self.response.json()['prices']
        return self.data

    def put_data(self, sheet_data):
        for i in range(0, len(sheet_data)):
            id_ = sheet_data[i]["id"]
            iata_code = sheet_data[i]["iataCode"]
            sheety_updated_endpoint = f"{SHEETY_ENDPOINT}/{id_}"
            params = {
                "price": {
                    "iataCode": iata_code,
                }
            }
            requests.put(url=sheety_updated_endpoint, auth=BASIC, json=params)
