# API Advanced - Reddit API Project

This project contains Python functions that interact with the Reddit API to retrieve and analyze data from various subreddits. The tasks demonstrate working with API endpoints, handling pagination, parsing JSON responses, and implementing recursive functions.

## Learning Objectives

- How to read API documentation to find the endpoints you're looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Requirements

- Python 3.4.3+
- Ubuntu 14.04 LTS
- PEP 8 style guide
- All files must be executable
- Must use the Requests module
- Custom User-Agent must be set to avoid rate limiting

## Files Description

| File | Description |
|------|-------------|
| `0-subs.py` | Returns the number of subscribers for a given subreddit |
| `1-top_ten.py` | Prints the titles of the first 10 hot posts for a given subreddit |
| `2-recurse.py` | Returns a list of titles of all hot articles using recursion |
| `3-count.py` | Prints a sorted count of given keywords in hot article titles |

## Function Prototypes

### Task 0 - Number of Subscribers
```python
def number_of_subscribers(subreddit)
