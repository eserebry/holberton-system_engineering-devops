#!/usr/bin/python3
import requests
''' Queries the Reddit API'''


def number_of_subscribers(subreddit):
    ''' Returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given returns 0 '''
    my_url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "My User Agent Request"}

    try:
        get_url = requests.get(my_url, headers=headers).json()
        return get_url.get("data").get("subscribers")
    except:
        return 0
