#!/usr/bin/python3
"""
Module that recursively counts keyword occurrences
in hot post titles.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively counts occurrences of words in titles.
    Prints sorted results.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            lower_word = word.lower()
            counts[lower_word] = counts.get(lower_word, 0)

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
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1

    after = data.get("after")

    if after:
        return count_words(subreddit, word_list, after, counts)

    # Final print
    sorted_counts = sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))
