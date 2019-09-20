#!/usr/bin/python3
"""
0. How many subs?
"""
import requests as r


def recurse(subreddit, hot_list=[]):
    """
    queries the Reddit API and returns the number of subscribers
    If an invalid subreddit is given, the function should return 0.
    """
    if (subreddit is not None and len(hot_list) == 0):
        headers = {"User-Agent": "APILearning"}
        url = "http://reddit.com/r/{}/hot.json"
        about = r.get(url.format(subreddit), headers=headers)
        if about.status_code != 200:
            print(None)
            return 0
        about = about.json()
        if about["kind"] == "Listing":
            hot_list.extend(about["data"]["children"])
            if (len(hot_list) == 0):
                return None
        else:
            return None
    else:
        if type(hot_list) == dict:
            hot_list = {}
            hot_list.append(hot_list[0]["data"]["title"])
    return hot_list
