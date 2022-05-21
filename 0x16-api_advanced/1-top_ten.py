#!/usr/bin/python3
"""Top ten"""
import requests


def top_ten(subreddit):
    """returns the top 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyApp/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get("data")
            children = data.get("children")
            for each in children[:10]:
                print(each.get("data").get("title"))
        except Exception as e:
            print("None")
    else:
        print("None")
