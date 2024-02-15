# import requests
# import json
# respond = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=ae357682672146ca889a4f745f71bd1f")
# print(respond.json());

# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(respond.json())


from newspaper import Article

url = "http:// timesofindia.indiatimes.com/world/china/chinese-expert-warns-of-troops-entering-kashmir/articleshow/59516912.cms"


toi_article = Article(url, language="en") # en for English

toi_article.parse()
toi_article.nlp()


print("Article's Title:")
print(toi_article.title)
print("n")

#To extract text
print("Article's Text:")
print(toi_article.text)
print("n")

#To extract summary
print("Article's Summary:")
print(toi_article.summary)
print("n")

#To extract keywords
print("Article's Keywords:")
print(toi_article.keywords)
