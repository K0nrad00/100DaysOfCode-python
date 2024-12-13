# from operator import index

from bs4 import BeautifulSoup

## EXPLENATION OF BS:
# with open("website.html") as f:
#     contents = f.read()
#     # print(contents)
#     # print(type(contents), len(contents))
#
# soup = BeautifulSoup(contents, 'html.parser') # sometimes its 'lxml' you need to use
#
# # print(soup.title) # test - tap as it was python object
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # print(soup.a) # first anchor tag in 'contents' html
# # print(soup.li)  # first list item in contents
# # print(soup.p)   # first paragraph in contents
#
# # Get all the anchor tags or paragraphs
# # use find_all() method from bs:
# all_anchor_tags = soup.find_all(name="a")
# all_paragraphs = soup.find_all(name="p")
# print(all_paragraphs)
# print(type(all_paragraphs)) # not a list, but like a list
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href")) # get the links from anchor tags
#
# heading = soup.find_all(name="h1", id="name") # more search examples, more attributes can be used
# print(heading)
#
# # alternate if you need one only h1 with name is to use find():
# head1 = soup.find(name="h1", id="name")
# print(head1)
#
# class_keyword_search = soup.find(name="h3", class_="heading") # class_ is used instead of class, class is reserved in Python
# print(class_keyword_search)
#
# # using CSS selectors
# company_url = soup.select_one(selector="p a") # first matching item .. here anchor that sits in paragraph
# print(company_url)
#
# # select all sections that use class="heading", also in CSS styling - . is for class # is for id
# all_classes = soup.select(".heading")
# print(all_classes)

# Easy mode: https://appbrewery.github.io/news.ycombinator.com/
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
# print(response.status_code)

yc_website = response.text # equivalent of having website locally

soup = BeautifulSoup(yc_website, "html.parser")
# print(soup.title) # test

# CHALLENGE: get title of first article using bsoup
# article_text = soup.find(name="span", class_="titleline")
# print(article_text)

article_tag = soup.find(name="a", class_="storylink")
print(article_tag)
article_text = article_tag.getText()
article_link = article_tag.get("href")
print(article_link)
# article_upvote = soup.select("#score_40725924")
article_upvote = soup.find(name="span", class_="score").getText()
print(article_upvote)




articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all("span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

# for item in article_upvotes:
#     score = item.split()[0]
#     print(score)
#
article_scores = [int(item.split()[0]) for item in article_upvotes]
print(article_scores)

# get the highest scored article and link for it from the list
max_score = max(article_scores)
index_max_score = article_scores.index(max_score)
print(max_score)
print(index_max_score)
print(f"The highest scored article is '{article_texts[index_max_score]}' ; link - '{article_links[index_max_score]}'")