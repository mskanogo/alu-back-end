#!/usr/bin/python3
"""
Module for recursively querying the Reddit API and returning all hot posts
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Returns a list of titles of all hot posts for a given subreddit using recursion
    """
    if hot_list is None:
        hot_list = []
    
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
                return hot_list if hot_list else None
            
            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))
            
            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list
        return None
    except requests.RequestException:
        return None
