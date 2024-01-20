import requests
from bs4 import BeautifulSoup
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