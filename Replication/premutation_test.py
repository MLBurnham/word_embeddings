########
# README
########
# This script performs a permutation test by randomly assigning the text labels and calculating cosine similarity
# Results are saved to a csv file

# Set the number of permutations in the environment section
# Set the number of threads in the environment section. For best results use the number of cores + 2
# Change which word you are testing in the permutation section

# 1000 permutations takes 12-14 hours to run at 6-10 threads. Double that time if you run permutations
# for both cosine similarity and relative cosine similarity

#####################
# Define Environment
#####################
import os
import pandas as pd
from gensim.models import Word2Vec
import random

from TextPrep import TextPrep
from get_cosine import cosine_sim

os.chdir('../Meta Data')
from key_words import key_words, key_synonyms
from stop_words import stop_words
os.chdir('..')

# set the number of threads
n_threads = 6

# set the number of permutations to run
permutations = 1000

#############################
# Import and pre-process data
#############################
tweet_df = pd.read_csv('Data/replication_text.csv')
# Create lists of text and labels
tweets = tweet_df['text']
labels = tweet_df['party']

# initialize parser for both keywords and base words
keyprep = TextPrep(stopwords = stop_words, key_words = key_words, key_synonyms = key_synonyms)
baseprep = TextPrep(stopwords = stop_words, key_words = base_words, key_synonyms = base_synonyms)
agreeprep = TextPrep(stopwords = stop_words, key_words = agree_words, key_synonyms = agree_synonyms)

# preprocess text
tweets = [keyprep.twitter_preprocess(tweet) for tweet in tweets]

#############################
# Permutation Test
#############################
# run the permutation test for cosine similarity
sim = []
for i in range(permutations):
    # permute the labels
    rlabels = random.sample(list(plabels), len(plabels))
    # Get cosine similarity
    rcosine = cosine_sim(parser = prep, keyword = 'trump', text = tweets, labels = rlabels, threads = n_threads)
    # append to list
    sim.append(rcosine)

# save results as a csv
simdf = pd.DataFrame(sim, columns = ['cosine similarity'])
simdf.to_csv('permutation.csv', index = False)

# run the permutation test for relative cosine similarity
relsim = []
for i in range(permutations):
    # permute the labels
    rlabels = random.sample(list(plabels), len(plabels))
    # Get cosine similarity
    rcosine = cosine_sim(parser = prep, keyword = 'trump', text = tweets, labels = rlabels, relative = True, threads = n_threads)
    # append to list
    relsim.append(rcosine)

# save results as a csv
relsimdf = pd.DataFrame(relsim, columns = ['relative cosine similarity'])
relsimdf.to_csv('relative_permutation.csv', index = False)