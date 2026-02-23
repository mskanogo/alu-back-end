#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit exists
    if response.status_code == 200:
        data = response.json()
        return data['data'].get('subscribers', 0)
    else:
        return 0
