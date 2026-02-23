#!/usr/bin/python3
import requests

def add_subscriber(subreddit, amount):
    """
    Adds 'amount' of subscribers to the subreddit.
    Returns the new number of subscribers, or None if invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    current_subs = data['data'].get('subscribers', 0)
    
    new_total = current_subs + amount
    # Ensure the total is not negative
    if new_total < 0:
        new_total = 0
    
    return new_total
