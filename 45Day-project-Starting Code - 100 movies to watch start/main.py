import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
web_content = response.text
# print(response.status_code)   # test
# print(web_content[0:100])     # test

soup = BeautifulSoup(web_content, "html.parser")
# print(soup.title) # test

# title_one = soup.find(name="h3", class_="title")  # test
# print(title_one.getText())                        # test


all_titles = soup.find_all(name="h3", class_="title")
list_of_titles = []

for title in reversed(all_titles):
    list_of_titles.append(title.getText())

# list_of_titles = list_of_titles[::-1] # ALTERNATE TO reversed()
# print(list_of_titles[::-1])
titles_for_file = "\n".join(list_of_titles)

with open("movies.txt", "w") as f:
    f.write(titles_for_file)

