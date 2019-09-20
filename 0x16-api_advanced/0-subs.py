#!/usr/bin/python3
"""
0. How many subs?
"""
import requests as r


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    If an invalid subreddit is given, the function should return 0.
    """
    headers = {"User-Agent": "Frocuts"}
    url = "http://reddit.com/r/{}/about.json"
    about = r.get(url.format(subreddit), headers=headers)

    if about.status_code != 200:
        return 0
    about = about.json()
    if about["kind"] == "t5":
        return about["data"]["subscribers"]
    else:
        return 0
