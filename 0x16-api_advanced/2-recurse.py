#!/usr/bin/python3
"""Queries the Reddit API and returns a list"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing
        the titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after)
    headers = {"User-Agent": "MyApp/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json().get("data")
            children = data.get("children")
            for each in children:
                hot_list.append(each.get("data").get("title"))
            after = data.get("after")
            if after is not None:
                recurse(subreddit, hot_list, after)
        except Exception as e:
            return hot_list
    else:
        return hot_list

    return recurse(subreddit, hot_list, after)
