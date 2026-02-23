#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Prints a sorted count of given keywords in the titles of all hot posts
    """
    if counts is None:
        counts = {}
        word_list = [word.lower() for word in word_list]
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:3-count.py:v1.0.0 (by /u/yourusername)"
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
            title = post.get("data", {}).get("title", "").lower().split()
            
            for word in word_list:
                word_lower = word.lower()
                # Count exact word matches only (no partial matches)
                count = title.count(word_lower)
                if count > 0:
                    counts[word_lower] = counts.get(word_lower, 0) + count
        
        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            if counts:
                # Sort by count (descending) and then alphabetically (ascending)
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
    return None
