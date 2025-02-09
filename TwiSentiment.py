import tweepy
from textblob import TextBlob


BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAFSrywEAAAAAxVsr%2B0STKw4PE05BkBZESGAmRBc%3DFEmV77Xf9bjPqjbtSPL7L3COl0uJwp24LrJZurrjBPGiPUMNy4"


client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = "Trump -is:retweet lang:en"


response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=["text"])


if response.data:
    for tweet in response.data:
        print("\nTweet:", tweet.text)

        # Sentiment Analysis
        analysis = TextBlob(tweet.text)
        print("Sentiment:", analysis.sentiment)
else:
    print("No tweets found.")

# All worked!