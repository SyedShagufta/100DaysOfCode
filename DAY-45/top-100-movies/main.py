from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_page = response.text

soup = BeautifulSoup(empire_page, "html.parser")

movie_list = [movie.getText() for movie in soup.findAll(name="h3", class_="title")]

with open("movie-list.txt", "w", encoding="utf-8") as file:
    for movie in movie_list[::-1]:
        file.write(movie+"\n")
