import requests
import tweepy
import json
import os
import csv
  
bearer_token = 'AAAAAAAAAAAAAAAAAAAAANuaowEAAAAAHKJUHauT6%2BOm4pRpStNPS8UgXo4%3DEzCwQRDNsVihMX1CZGYlwhDVFSWEiXLy6a5i60drxUi2A8rDTo'

#Defining a function to authenticate requests:
def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers
    
#Define function to build the API request URL:

def create_url(query, max_results):
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results={max_results}&tweet.fields=created_at,lang"
    return url

def get_tweets(url, headers, next_token=None):
    if next_token:
        url += f"&next_token={next_token}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}")
    return response.json()

query = 'transparency OR trust OR finance'
max_results = 100  # Maximum tweets per request
total_tweets = 500  # Total tweets to collect
tweets = []

headers = create_headers(bearer_token)

while len(tweets) < total_tweets:
    if len(tweets) == 0:
        url = create_url(query, max_results)
        tweets_data = get_tweets(url, headers)
    else:
        next_token = tweets_data['meta'].get('next_token', None)
        if not next_token:
            break
        tweets_data = get_tweets(url, headers, next_token)
    tweets.extend([tweet['text'] for tweet in tweets_data['data']])
    
# Save the tweets to a file
with open('tweets_v2.json', 'w') as f:
    json.dump(tweets, f)

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'