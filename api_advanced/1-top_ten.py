#!/usr/bin/python3
"""
Module that queries the Reddit API and prints
the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Prints the top 10 hot post titles of a subreddit.
    If invalid subreddit, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])

    for post in posts:
        print(post.get("data", {}).get("title"))
