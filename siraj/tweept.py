import tweepy
import textblob

consumer_key = "DEHk9kDCWjZeP2rD3oYIMJT7l"
consumer_secret = "kdxFH7U8sQBpL5q7g2ujzk1bm033TUeF5o320FgXUV7aUIkEKi"

access_token = "903928713343102976-AOv7IGe2SKtg54UO0DPimBF8qhUMDmh"
access_token_secret = "VnjIHwJrTYsOADxcnZBeb6JWrYwPfK5Lfc0UcTrKosS1f"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print "\n" + tweet.text
    analysis = textblob.TextBlob(tweet.text)
    print analysis.sentiment