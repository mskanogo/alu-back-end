#!/usr/bin/python3
import requests

def is_subscriber(subreddit, user):
    """
    Checks if the authenticated user is subscribed to the subreddit.
    Returns True if subscribed, False otherwise.
    """
    # Note: Requires OAuth authentication with Reddit API
    url = "https://oauth.reddit.com/subreddits/mine/subscriber"
    headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN', 'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return False
    
    data = response.json()
    for subreddit_info in data.get('data', {}).get('children', []):
        if subreddit_info['data']['display_name'].lower() == subreddit.lower():
            return True
    return False
