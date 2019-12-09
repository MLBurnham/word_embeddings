library(dplyr)
library(ggplot2)
library(tidyr)
setwd("/home/mike/Desktop/Word Embeddings")

# Read in data
# still need to subset to data after date
text <- read.csv('Data/aggregated_tweets.csv')
meta <- read.csv('Meta Data/meta_data.csv')
keysim <- read.csv('Analysis/keyword_similarity.csv')
basesim <- read.csv('Analysis/baseword_similarity.csv')
agreesim <- read.csv('Analysis/agreeword_similarity.csv')
tweets <- left_join(text, meta, by = 'user_id')
rm(text, meta)

# subset and reformat tweets
tweets <- tweets[tweets$party == 'R' | tweets$party == 'D',]
ggtweets <- count(tweets, party)

# combine cosine data into single df
agreesim$label <- 'Agree'
basesim$label <- 'Base'
keysim$label <- 'Disagree'
cosim <- bind_rows(keysim, agreesim, basesim)

# distribution of tweets by party
ggplot(data=ggtweets, aes(x=party, y=n, fill=party)) +
  geom_bar(stat="identity", position=position_dodge(), colour="black", size = .3) +
  scale_fill_manual(values = c("#0072B2", "#D55E00")) +
  labs(title = "Tweets by Party", x = "Party", y = 'Tweets', fill = 'Party')+
  geom_text(aes(label=n), vjust=-.3, color="black", size=4.5)+
  theme_classic() +
  theme(plot.title = element_text(hjust = 0.5))
  
# histogram for permutation tests
ggplot(mpg, aes(displ)) + scale_fill_brewer(palette = "Spectral") + 
  geom_histogram(aes(fill=class), 
                   binwidth = .1, 
                   col="black", 
                   size=.1) +  # change binwidth
  labs(title="Histogram with Auto Binning", 
       subtitle="")  

# Density plot for t-test
ggplot(data = cosim, aes(similarity)) + geom_density(aes(fill=factor(label)), alpha=0.8) + 
  labs(title="Distribution: Density Plot", 
       subtitle="Cosine Similarity Grouped by Category",
       x="Cosine Similarity",
       y="Density",
       fill="Word Category")

  # box plot for t-test
cosimsum <- cosim %>% 
  group_by(label) %>%
  summarise(Mean = mean(similarity), Max = max(similarity), Min = min(similarity))

box <- ggplot(data = cosim, aes(label, similarity))

box + geom_boxplot() + 
  geom_dotplot(binaxis='y', 
               stackdir='center', 
               dotsize = .5, 
               fill="red") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6)) + 
  labs(title="Distribution: Box Plot", 
       subtitle="Cosine Similarity by Word Category",
       x="Word Category",
       y="Cosine Similarity") +
  theme_bw()
