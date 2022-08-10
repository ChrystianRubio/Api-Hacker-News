import requests
from operator import itemgetter


url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)


submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:10]:
    # doing another call for each one

    url = (f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()


    submission_dict = {
        'title': response_dict['title'],
        'link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)

for each in submission_dicts:
    print('#' * 80, "\n")
    print(f"Title: {each['title']}")
    print(f"Link: {each['link']}")
    print(f"Comments: {each['comments']}\n")
