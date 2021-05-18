#!/usr/bin/python3
"""Queries Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return: Number of subcribers for given subreddit
    0 if invalid subreddit
    """
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-agent": "custom"}
    r = requests.get(URL, headers=headers)
    if(r.status_code == 200):
        return r.json()["data"]["subscribers"]
    return 0
