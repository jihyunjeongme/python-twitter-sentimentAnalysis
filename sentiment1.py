#Import libraries
import tweepy
from textblob import TextBlob

#Create your app from apps.twitter.com and fill your keys and tokens
consumer_key = '8Xo1W6GDM3LgNpOytlOFUqdHl**'
consumer_secret = 'I7yGwNEpbMpy0kXPqeDBb460u8lrm9Pc89B80Y2kT3lgvy4MhI**'
access_token = '161519296-KxGq3wRErhbsok4kpEEcvNXMA7l4gaasvvK06a0J**'
access_token_secret = 'TQSd6Rcw4XtLqHNMTMiFbvam2KBwBSOf6wb2GUt5FilP5**'

#Authenticate your application
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Search for tweets
public_tweets = api.search('Seoul')
for tweet in public_tweets:
    #Print tweets
    print(tweet.text)
    #Use textblob to fetch sentiment of the tweet
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('\n')



