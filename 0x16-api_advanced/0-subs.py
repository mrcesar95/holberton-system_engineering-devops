#!/usr/bin/python3
"""reddit api"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a subreddit"""

    url = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "platform"},
        allow_redirects=False)
    if url.status_code == 200:
        return int(url.json().get("data").get("subscribers"))
    else:
        return 0
