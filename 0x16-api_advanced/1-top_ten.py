#!/usr/bin/python3
import requests
''' Queries the Reddit API'''


def top_ten(subreddit):
    ''' prints the titles of the first 10 hot posts
    listed for a given subreddit.'''

    my_url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers = {"User-Agent": "My User Agent Request"}

    try:
        get_url = requests.get(my_url, headers=headers).json()
        children = get_url.get("data").get("children")
        for child in children:
            print(child.get("data").get("title"))
    except:
        print(None)
