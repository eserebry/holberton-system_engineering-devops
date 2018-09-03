#!/usr/bin/python3
import requests
''' Queries the Reddit API'''


def recurse(subreddit, hot_list=[], after=""):
    ''' returns a list of  the titles of all hot articles
    for a given subreddit. If no results are found returns None.'''

    m_url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "My User Agent Request"}

    try:
        get_url = requests.get(m_url, headers=headers).json()
        children = get_url.get("data").get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))
        after = get_url.get("data").get("after")
        return recurse(subreddit, hot_list, after)
    except:
        return None
