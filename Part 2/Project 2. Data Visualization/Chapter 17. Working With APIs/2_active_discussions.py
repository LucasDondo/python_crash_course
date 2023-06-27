import requests
import json
from operator import itemgetter
import plotly.express as px

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
top_stories_ids = r.json()

status_code = str(r.status_code)
if status_code == "200":
    status_code += " 👍🏻"
else:
    status_code += " 👎🏻"
#
print(f"Status code: {status_code}")

top_stories = []
for top_story_id in top_stories_ids[:10]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json"
    r = requests.get(url)
    top_story = r.json()
    d = {
        "title": top_story["title"],
        "url": top_story["url"],
        "q_comments": top_story["descendants"],
    }
    top_stories.append(d)
top_stories.sort(key=itemgetter("q_comments"), reverse=True)
#
titles, urls, q_comments = [], [], []
for top_story in top_stories:
    titles.append(f"<a href='{top_story['url']}'>{top_story['title']}</a>")
    q_comments.append(top_story["q_comments"])

fig = px.bar(
    x=titles,
    y=q_comments,
    title="Most Active Discussions on Hacker News",
    labels={"x": "Discussion", "y": "Number of Comments"},
)
fig.show()
