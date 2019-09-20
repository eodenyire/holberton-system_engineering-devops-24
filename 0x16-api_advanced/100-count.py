#!/usr/bin/python3
"""
0. How many subs?
"""
import requests as r
from sys import argv


def count_words(subreddit, word_list, key=""):
    """
    queries the Reddit API and returns the number of subscribers
    If an invalid subreddit is given, the function should return 0.
    """
    headers = {"User-Agent": "Frocuts"}
    url = "http://reddit.com/r/{}/hot.json?after={}"
    about = r.get(url.format(subreddit, key), headers=headers)
    if about.status_code != 200:
        print(None)
        return 0
    about = about.json()
    if about["kind"] == "Listing":
        #for data in about["data"]["children"]:
            # print(data["data"]["title"])
        for word in word_list:
            print('{}: {}'.format(word, 0))
    else:
        print(None)
