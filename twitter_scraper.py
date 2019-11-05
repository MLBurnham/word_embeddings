import tweepy
import pandas as pd

class twitter_scraper:
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        """
        Class for scraping tweets from twitter's resting API.
        Pass a set of consumer and access keys
        """
        self.auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(self.auth)
        
    def original_tweet(self, status):
        """
        Check if a tweet is original or a retweet/reply. 
        
        """
        if hasattr(status, 'retweeted_status'):
            return False
        elif status.in_reply_to_status_id != None:
            return False
        elif status.in_reply_to_screen_name != None:
            return False
        elif status.in_reply_to_user_id != None:
            return False
        else:
            return True
    
    def pull_tweets(self, twitter_id, count = 200, since = None, tweet_mode = 'extended'):
        """
        Scrapes twitter the twitter timeline for original tweets from the given twitter id and returns them as a list of status objects
        Default is set to 200 most recent tweets.
        If you want to pull from a specific tweet pass a tweet ID to the 'since' variable
        """
        user_tweets = self.api.user_timeline(user_id = twitter_id, count = count, since_id = since, tweet_mode = tweet_mode)
        user_tweets = [tweet for tweet in user_tweets if self.original_tweet(tweet) == True]
        return user_tweets
    
    def tweets_to_df(self, tweet_list):
        """
        Convert a list of tweet objects to a pandas data frame
        columns include: tweet id, tweet text, date created, retweet, and user id
        """
        tweet_ids = []
        tweet_texts = []
        created_at = []
        retweet = []
        user_id = []

        for tweet in tweet_list:
            tweet_ids.append(tweet.id)
            tweet_texts.append(tweet.full_text)
            created_at.append(tweet.created_at)
            retweet.append(tweet.retweeted)
            user_id.append(tweet.user.id)

        tweets_df = pd.DataFrame(zip(tweet_ids, tweet_texts, created_at, retweet, user_id), columns = ["tweet_id", 'text', 'created', 'retweet', 'user_id'])
        return tweets_df