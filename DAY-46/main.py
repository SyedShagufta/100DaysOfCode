import os
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
# input the year in the format YYYY-MM-DD
year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup)
# scrape the 100 song titles on that date into a python list
songs = soup.select("li ul li h3")
songs_titles = [song.getText().strip() for song in songs]
print(songs_titles)

# Authorizing to spotify
scope = "user-library-read user-read-playback-state user-read-currently-playing"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="wtwiwyjv6iqlgcbok1sbo3m4e",
    )
)
user_id = sp.current_user()["id"]
print(user_id)
