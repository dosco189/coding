import tweepy
import csv

# Twitter API credentials
consumer_key = "90z8DLK2KnMM6ahpCeahScSQl"
consumer_secret = "EtdilnurvMEI7izJg4DKjIeSXcD402hDKmtPlsUfyAU1WNbW9y"
access_token = "2677582184-ucJjYrr4SkzTDLcSk9PY5GGe2YEyNVFoWdfQw5P"
access_token_secret = "UjlmtObbMN2OUwDgutt21poBOsJeB0S007ToGmuLK6pdz"

# Authenticate to the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Search parameters
keywords = ["trust", "transparency", "finance"]
start_date = "2022-01-01"
end_date = "2023-12-31"
tweet_limit = 500

# Perform the search
tweets = tweepy.Cursor(api.search_tweets,
                       q=" OR ".join(keywords),
                       lang="en",
                       since=start_date,
                       until=end_date,
                       tweet_mode="extended").items(tweet_limit)

# Create and open a CSV file for writing
with open("tweets.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Account", "Tweet"])  # Write header row

    # Write tweet data to the CSV file
    for tweet in tweets:
        writer.writerow([tweet.user.screen_name, tweet.full_text.replace('\n', ' ')]) 

print("Tweets exported successfully to tweets.csv.")