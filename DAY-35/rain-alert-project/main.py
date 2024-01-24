import os

import requests, time, schedule
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ['api_key']
account_sid = os.environ['TWILLIO_ACCOUNT_SID']
auth_token = os.environ['TWILLIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def telegram_bot_sendtext(bot_message):
    bot_token = os.environ['bot_token']
    bot_chatID = os.environ['bot_chatId']
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

weather_params = {
    # "lat": 17.492680,
    # "lon": 78.405390,
    "lat": 41.878113,
    "lon": -87.629799,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    my_message = "It might Rain today 🌧️⛈️.. \n \n Make sure you carry your Umbrella ☔☔. \n \n \n With Love, By Sofia 💖"
    telegram_bot_sendtext(my_message)

    # message = client.messages \
    #     .create(
    #     body="It might Rain today 🌧️⛈️.. Make sure you carry your Umbrella ☔☔. \n With Love, By Sofia 💖",
    #     from_='+14157989642',
    #     to='my_phone_num'
    # )

    # print(message.status)
