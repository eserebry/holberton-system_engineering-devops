#!/usr/bin/python3
import requests
''' Queries the Reddit API'''


def count_words(subreddit, word_list):
    ''' parses the title of all hot articles,
    and prints a sorted count of given keywords'''

    my_url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {"User-Agent": "My User Agent Request"}

    try:
        get_url = requests.get(my_url, headers=headers).json()
        after = after = get_url.get("data").get("after")
        if after:
            my_url = my_url + "?after={}".format(after)
        children = get_url.get("data").get("children")
        for child in children:
            child.append(child.get("data").get("title"))
        after = get_url.get("data").get("after")
        if after is None:
            return count
        return count_words(subreddit, word_list)
    except:
        return None
