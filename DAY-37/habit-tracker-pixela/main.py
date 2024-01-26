# Create a new pixela user
import os

import requests
from datetime import datetime
TOKEN = os.environ['token']
USERNAME = "sofia26"
PIXELA_API_ENDPOINT = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": "sofia26",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_API_ENDPOINT, json=params)
# print(response.text)

GRAPH_ENDOINT = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs"

# create a graph
graph_header = {
    "X-USER-TOKEN": TOKEN,
}
graph_params = {
    "id": "mygraph1",
    "name": "Coding Graph",
    "unit": "hr",
    "type": "int",
    "color": "ajisai",
}

# response = requests.post(url=GRAPH_ENDOINT, json=graph_params, headers=graph_header)
# print(response.text)

# adding a pixel
GRAPH_ID = "mygraph1"
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
print(formatted_date)

NEW_GRAPH_ENDPOINT = f"{GRAPH_ENDOINT}/{GRAPH_ID}"
new_graph_params = {
    "date": "20231208",
    "quantity": "3"
}

# response = requests.post(url=NEW_GRAPH_ENDPOINT, json=new_graph_params, headers=graph_header)
# print(response.text)
