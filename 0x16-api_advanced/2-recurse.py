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
        h = {"User-Agent": "Frocuts"}
        url = "http://reddit.com/r/{}/hot.json"
        p = {'after': key}
        about = r.get(url.format(subreddit), headers=h, params=p)
        if about.status_code != 200:
            return None
        about = about.json()
        # hot_list.extend(about["data"]["children"])
        hot_list.extend([x.get('data').get('title')
                        for x in about["data"]["children"]])
        if about['data']['after'] is not None:
            recurse(subreddit, hot_list, about['data']['after'])
        if (len(hot_list) > 0):
            return hot_list
        return None
    else:
        return None
