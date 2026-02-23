#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Returns a list of the titles of the top 10 hot posts in a subreddit.
    If the subreddit is invalid or has no hot posts, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if subreddit exists
    if response.status_code != 200:
        return None
    
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    
    if not posts:
        return None
    
    # Extract titles of top 10 hot posts
    top_titles = [post['data']['title'] for post in posts]
    return top_titles
