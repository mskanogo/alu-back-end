#!/usr/bin/python3
"""
Module for recursively querying the Reddit API and counting keywords in hot posts
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Prints a sorted count of given keywords in the titles of all hot posts
    """
    if counts is None:
        counts = {}
        # Convert all words to lowercase and remove duplicates for counting
        word_list = [word.lower() for word in word_list]
    
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    params = {
        'limit': 100,
        'after': after
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')
            
            if not posts and after is None:
                if counts:
                    # Sort by count (descending) then alphabetically (ascending)
                    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                    for word, count in sorted_counts:
                        print("{}: {}".format(word, count))
                return
            
            for post in posts:
                title = post.get('data', {}).get('title', '').lower().split()
                
                # Count each word in the title
                for word in title:
                    # Remove any punctuation from the word
                    clean_word = ''.join(c for c in word if c.isalnum())
                    if clean_word in word_list:
                        counts[clean_word] = counts.get(clean_word, 0) + 1
            
            if after is not None:
                return count_words(subreddit, word_list, after, counts)
            else:
                if counts:
                    # Sort by count (descending) then alphabetically (ascending)
                    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                    for word, count in sorted_counts:
                        print("{}: {}".format(word, count))
        return None
    except requests.RequestException:
        return None
