#!/usr/bin/python3
"""2-recurse module"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-agent": "custom"}
    params = {'after': after}

    res = requests.get(URL, headers=headers, params=params,
                       allow_redirects=False).json()
    after = res['data']['after']
    for item in res['data']['children']:
        hot_list.append(item['data']['title'])
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list if len(hot_list) > 0 else None
