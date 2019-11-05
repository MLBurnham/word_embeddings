# Get the most recent tweet from all users
# Import unique IDs
aggregated_tweets = pd.read_csv('aggregated_tweets.csv')
unique_ids = aggregated_tweets['user_id'].unique()

# Get the last tweet for each unique ID
last_tweets = []
for user in unique_ids:
    last_tweet = max(aggregated_tweets[aggregated_tweets['user_id'] == user]['tweet_id'])
    last_tweets.append(last_tweet)

# Pass to a dictionary of IDs and their most recent tweet
last_tweet_dict = dict(zip(unique_ids, last_tweets))

# initialize scraper
scraper = twitter_scraper(consumer_key, consumer_secret, access_token, access_secret)

# import congress twitter user IDs 
congress_meta = pd.read_csv('congress_meta_data.csv')
congress_ids = congress_meta['id']

# loop through each member of congress and append their tweets to a list
tweets = []
for key, value in last_tweet_dict.items():
    user_tweets = scraper.pull_tweets(key, since = value)
    tweets = tweets + user_tweets

# Convert the tweets to a dataframe 
tweets_df = scraper.tweets_to_df(tweets)
tweets_df.to_csv('congressional_tweets_' + datetime.now().strftime('%Y_%m_%d_%H_%M') + '.csv', index = False)

# Merge new tweets with previously aggregated tweets and write to csv
merged_tweets = pd.concat([aggregated_tweets, tweets_df])
merged_tweets.to_csv('aggregated_tweets.csv', index = False)