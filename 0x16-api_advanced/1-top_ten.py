#!/usr/bin/python3
""" Queries the Reddit API and returns the number """
import requests


def top_ten(subreddit):
    """ Returns the number of subscribers for a given subreddit. """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36(KHTML, like Gecko)'
        'Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print(None)
        return

    data = response.json().get('data').get('children')
    for i in range(10):
        print(data[i].get('data').get('title'))
