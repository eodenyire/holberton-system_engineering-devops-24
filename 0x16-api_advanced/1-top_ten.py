#!/usr/bin/python3
"""
0. How many subs?
"""
import requests as r


def top_ten(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    If an invalid subreddit is given, the function should return 0.
    """
    headers = {"User-Agent": "Frocuts"}
    url = "http://reddit.com/r/{}/hot.json?limit=10"
    about = r.get(url.format(subreddit), headers=headers)
    if about.status_code != 200:
        print(None)
        return 0
    about = about.json()
    if about["kind"] == "Listing":
        for data in about["data"]["children"]:
            print(data["data"]["title"])
    else:
        print(None)
