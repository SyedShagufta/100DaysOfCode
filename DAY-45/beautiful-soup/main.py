from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.findAll(name="span", class_="titleline")
article_votes = [int(score.getText().split('points')[0]) for score in soup.findAll(name="span", class_="score")]

article_text = []
article_links = []

for tag in article_tag:
    article_text.append(tag.getText())
    article_links.append(tag.contents[0].get("href"))

# print(article_text)
# print(article_links)
# print(article_votes)

# Print the title and link of the highest number of upvote
index_of_max_upvotes = article_votes.index(max(article_votes))
print(index_of_max_upvotes)

print(f"The highest number of upvotes are for the below title: {article_text[index_of_max_upvotes]} and the link is"
      f" {article_links[index_of_max_upvotes]}")
