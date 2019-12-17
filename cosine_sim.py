########
# README
########
# This script calculates cosine similarity or relative cosine similarity for all words in the key_words.py list
# and saves the results in CSV files.
# Because this is a lengthy computation it is broken into parts. 

# The cosine_sim function is capable of multi-threading. 
# To adjust the number of threads used, set the n_threads variable in the Define Environment section

# The entire script will take roughly 4-6 hours on most computers.


#####################
# Define Environment
#####################
import os
import pandas as pd
from gensim.models import Word2Vec

from TextPrep import TextPrep
from cosine_function import cosine_sim

os.chdir('./Meta Data')
from key_words import key_words, key_synonyms, base_words, base_synonyms, agree_words, agree_synonyms
from stop_words import stop_words
os.chdir('..')

# set the number of threads
n_threads = 6

#############################
# Import and pre-process data
#############################
# load in data
meta_data = pd.read_csv('Meta Data/meta_data.csv')
tweet_df = pd.read_csv('Data/replication_text.csv')
# merge data with meta data
tweet_df = pd.merge(tweet_df, meta_data, how = 'inner', on = 'user_id')
tweet_df = tweet_df[tweet_df.party.isin(['R', 'D'])].reset_index(drop=True)
# Create lists of text and labels
tweets = tweet_df['text']
labels = tweet_df['party']

# initialize parser for both keywords and base words
keyprep = TextPrep(stopwords = stop_words, key_words = key_words, key_synonyms = key_synonyms)
baseprep = TextPrep(stopwords = stop_words, key_words = base_words, key_synonyms = base_synonyms)
agreeprep = TextPrep(stopwords = stop_words, key_words = agree_words, key_synonyms = agree_synonyms)

# preprocess text
tweets = [keyprep.twitter_preprocess(tweet) for tweet in tweets]


####################
# Cosine Similarity
####################
# get cosine similarity for all words in the key word list
keysim = []
for word in key_words:
    try:
        cosine = cosine_sim(parser = keyprep, keyword = word, text = tweets, labels = labels, threads = n_threads)
        keysim.append(cosine)
    except Exception as e:
        print(e)
        print('failed at ' + word)

# Convert to dataframe
keysimdf = pd.DataFrame(data=list(zip(key_words, keysim)), columns = ['word', 'similarity'])
keysimdf.to_csv('Data/keyword_similarity.csv', index = False)

# get cosine similarity for all words in the base word list
basesim = []
for word in base_words:
    try:
        cosine = cosine_sim(parser = baseprep, keyword = word, text = tweets, labels = labels, threads = n_threads)
        basesim.append(cosine)
    except Exception as e:
        print(e)
        print('failed at ' + word)
# Convert to dataframe
basesimdf = pd.DataFrame(data=list(zip(base_words, basesim)), columns = ['word', 'similarity'])
basesimdf.to_csv('Data/baseword_similarity.csv', index = False)

# get cosine similarity for all words in the agree word list
agreesim = []
for word in agree_words:
    try:
        cosine = cosine_sim(parser = agreeprep, keyword = word, text = tweets, labels = labels, threads = n_threads)
        agreesim.append(cosine)
    except Exception as e:
        print(e)
        print('failed at ' + word)
# Convert to dataframe
basesimdf = pd.DataFrame(data=list(zip(agree_words, agreesim)), columns = ['word', 'similarity'])
basesimdf.to_csv('Data/agreeword_similarity.csv', index = False)

############################
# Relative Cosine Similarity
############################
# get relative cosine similarity for all words in the key word list
keyrelsim = []
for word in key_words:
    try:
        cosine = cosine_sim(parser = keyprep, keyword = word, text = tweets, labels = labels, threads = n_threads, relative = True)
        keyrelsim.append(cosine)
    except Exception as e:
        print(e)
        print('failed at ' + word)

# Convert to dataframe
keyrelsimdf = pd.DataFrame(data=list(zip(key_words, keyrelsim)), columns = ['word', 'relative_similarity'])
keyrelsimdf.to_csv('Data/keyword_relative_similarity.csv', index = False)

# get relative cosine similarity for all words in the base word list
baserelsim = []
for word in base_words:
    try:
        cosine = cosine_sim(parser = baseprep, keyword = word, text = tweets, labels = labels, threads = n_threads, relative = True)
        baserelsim.append(cosine)
    except Exception as e:
        print(e)
        print('failed at ' + word)
# Convert to dataframe
baserelsimdf = pd.DataFrame(data=list(zip(base_words, baserelsim)), columns = ['word', 'relative_similarity'])
baserelsimdf.to_csv('Data/baseword_relative_similarity.csv', index = False)

# get relative cosine similarity for all words in the agree word list
agreerelsim = []
for word in agree_words:
    try:
        cosine = cosine_sim(parser = agreeprep, keyword = word, text = tweets, labels = labels, threads = n_threads, relative = True)
        agreerelsim.append(cosine)
    except Exception as e:
        print(e)
        print('failed at ' + word)
# Convert to dataframe
agreerelsimdf = pd.DataFrame(data=list(zip(agree_words, agreerelsim)), columns = ['word', 'relative_similarity'])
agreerelsimdf.to_csv('Data/agreeword_relative_similarity.csv', index = False)