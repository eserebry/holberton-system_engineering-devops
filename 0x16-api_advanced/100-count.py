#!/usr/bin/python3
import requests
''' Queries the Reddit API'''


def count_words(subreddit, word_list):
    ''' parses the title of all hot articles,
    and prints a sorted count of given keywords'''

    m_url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "My User Agent Request"}
    try:
        get_url = requests.get(m_url, headers=headers).json()
        children = get_url.get("data").get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))
        after = get_url.get("data").get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except:
        return None
