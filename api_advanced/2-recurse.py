#!/usr/bin/python3
"""
Module that recursively queries the Reddit API
and returns all hot post titles for a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively collects all hot post titles.
    Returns list of titles or None if invalid subreddit.
    """
    headers = {"User-Agent": "alu-api-advanced"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
