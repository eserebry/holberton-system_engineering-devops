#!/usr/bin/python3
import requests
''' Queries the Reddit API'''


def number_of_subscribers(subreddit):
    ''' Returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given returns 0 '''
    my_url = "https://www.reddit.com/r/{}/about".format(subreddit)
    headers = {"My User-Agent": "My User Agent Request"}

    try:
        get_url = requests.get(my_url, headers=headers).json()
        return get_url['data']['subscribers']
    except:
        return 0
