# API Advanced

Python scripts that query the Reddit API to retrieve and analyze subreddit data.

## Files

- **0-subs.py** - Returns the number of subscribers for a given subreddit
- **1-top_ten.py** - Prints the top 10 hot post titles for a given subreddit
- **2-recurse.py** - Recursively returns a list of all hot post titles for a given subreddit
- **3-count.py** - Counts and prints sorted keyword occurrences in hot post titles

## Usage

```bash
python3 0-main.py <subreddit>
python3 1-main.py <subreddit>
python3 2-main.py <subreddit>
python3 3-main.py <subreddit> '<list of keywords>'
```

## Requirements

- Python 3
- `requests` module

