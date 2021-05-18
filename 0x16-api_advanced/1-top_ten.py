#!/usr/bin/python3
"""1-top_ten module"""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts listed for given subreddit"""
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-agent": "custom"}
    params = {'limit': 10}
    r = requests.get(URL, headers=headers, params=params)

    if(r.status_code == 200):
        posts = r.json()["data"]["children"]
        for each in posts:
            print(each["data"]["title"])
    else:
        print("None")
