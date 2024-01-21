import os
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
# input the year in the format YYYY-MM-DD
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup)
# scrape the 100 song titles on that date into a python list
songs = soup.select("li ul li h3")
songs_titles = [song.getText().strip() for song in songs]
# print(songs_titles)

# Authorizing to spotify
scope = "user-library-read user-read-playback-state user-read-currently-playing playlist-modify-private playlist-modify-public"
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

# Searching spotify for song by titles
song_uris = []
year = date.split("-")[0]
for song in songs_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print(song_uris)
# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
