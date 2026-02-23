#!/usr/bin/python3
"""Recursively counts keyword occurrences in hot post titles."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Recursively query Reddit API and count keyword occurrences in titles."""
    if not counts:
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1

    next_after = data.get("after")
    if next_after is None:
        results = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in results:
            if count > 0:
                print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, counts, next_after)
