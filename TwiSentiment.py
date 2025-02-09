import tweepy
from textblob import TextBlob


consumer_key = 'G1Q3InwWo2tB7jdE9oB0l8DkE'
consumer_secret = 'aHycN4nz31vkDJv1VSuG5yZXrr05EiJ6CvFoV2qdUFZEeS4AAC'

access_token = '2223589345-WaBPuaRIAMm4xuAgZwvwRzR5Vctb4Ww6sxVBmfI'
access_token_secret = 'jrcjfoQMCfPV6FjX1k7QjYOsv1PmkkvAga2JhU6Poxzhf'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
