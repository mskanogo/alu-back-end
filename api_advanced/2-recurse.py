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
    return recurse(subreddit, hot_list, next_after)#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Returns a list of titles of all hot posts for a given subreddit
    """
    if hot_list is None:
        hot_list = []
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:2-recurse.py:v1.0.0 (by /u/yourusername)"
    }
    params = {
        "limit": 100,
        "after": after
    }
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after")
        
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
        
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
