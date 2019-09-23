#!/usr/bin/python3
"""
0. How many subs?
"""
import requests as r


def recurse(subreddit, hot_list=[], key=""):
    """
    queries the Reddit API and returns the number of subscribers
    If an invalid subreddit is given, the function should return 0.
    """
    if (subreddit is not None):
        headers = {"User-Agent": "Frocuts"}
        url = "http://reddit.com/r/{}/hot.json?after={}"
        about = r.get(url.format(subreddit, key), headers=headers)
        if about.status_code != 200:
            return None
        about = about.json()
        if about["kind"] == "Listing":
            hot_list.extend(about["data"]["children"])
            if (len(hot_list) == 0):
                return None
        else:
            return None
    try:
        if type(hot_list) == dict:
            hot_list.append(hot_list[0]["data"]["title"])
            hot_list.pop(0)
            if about['data']['after'] is not None:
                recurse(subreddit, hot_list, about['data']['after'])
        return hot_list
    except Expection:
        return None
