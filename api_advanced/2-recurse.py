#!/usr/bin/python3
"""Module to recursively retrieve all hot post titles for a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively return a list of all hot post titles for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    posts = data.get("children", [])
    if not posts:
        return hot_list if hot_list else None
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    next_after = data.get("after")
    if next_after is None:
        return hot_list
    return recurse(subreddit, hot_list, next_after)
