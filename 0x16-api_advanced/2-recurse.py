#!/usr/bin/python3
""" Using reddit's API to get the top 10 hot posts of a subreddit """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36(KHTML, like Gecko)'
        'Chrome/58.0.3029.110 Safari/537.36'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
