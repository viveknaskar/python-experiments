import json
import time
import random

# Load the URL mapping from the JSON file
def load_url_mapping():
    with open('url_mapping.json', 'r') as f:
        return json.load(f)

# Save the URL mapping to the JSON file
def save_url_mapping(url_mapping):
    with open('url_mapping.json', 'w') as f:
        json.dump(url_mapping, f)

# Generate a shortened URL
def generate_short_url():
    # Use a combination of a randomly generated string and a timestamp to create a unique shortened URL
    return f"{int(time.time())}_{random.randint(1000000, 9999999)}"

# Shorten a URL
def shorten_url(original_url):
    url_mapping = load_url_mapping()

    # Check if the original URL is already in the mapping
    if original_url in url_mapping:
        return url_mapping[original_url]

    # Generate a new shortened URL
    short_url = generate_short_url()

    # Save the mapping to the database
    url_mapping[original_url] = short_url
    save_url_mapping(url_mapping)

    return short_url

# Expand a shortened URL
def expand_url(short_url):
    url_mapping = load_url_mapping()

    # Find the original URL in the mapping
    for original_url, url in url_mapping.items():
        if url == short_url:
            return original_url

    return None