# libraries
library(dplyr)
library(ggplot2)
library(tidyr)


################################
# Data Import and Manipulation
###############################
# Raw text
text <- read.csv('Data/replication_text.csv')

# Cosine similarity results
keysim <- read.csv('Analysis/keyword_similarity.csv')
basesim <- read.csv('Analysis/baseword_similarity.csv')
agreesim <- read.csv('Analysis/agreeword_similarity.csv')

# Single word permutation data
perm <- read.csv('Analysis/permutation.csv')

# generate tweet count table
ggtweets <- count(tweets, party)

# combine cosine data into single df
agreesim$label <- 'Agree'
basesim$label <- 'Base'
keysim$label <- 'Disagree'
cosim <- bind_rows(keysim, agreesim, basesim)

############
# Plots
############
# distribution of tweets by party
ggplot(data=ggtweets, aes(x=party, y=n, fill=party)) +
  geom_bar(stat="identity", position=position_dodge(), colour="black", size = .3) +
  scale_fill_manual(values = c("#0072B2", "#D55E00")) +
  labs(title = "Tweets by Party", x = "Party", y = 'Tweets', fill = 'Party')+
  geom_text(aes(label=n), vjust=-.3, color="black", size=4.5)+
  theme_classic()

ggsave("Analysis/tweetcount.png", device = "png")

# Density plot of cosine similarity
ggplot(data = cosim, aes(similarity)) + geom_density(aes(fill=factor(label)), alpha=0.8) + 
  labs(title="Distribution: Density Plot", 
       subtitle="Cosine Similarity Grouped by Category",
       x="Cosine Similarity",
       y="Density",
       fill="Word Category")

ggsave("Analysis/density.png", device = "png")

# Box plot of cosine similarity
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

ggsave("Analysis/boxplot.png", device = "png")

# Histogram of single word permutation

ggplot(perm, aes(x=cosine.similarity)) + 
  geom_histogram(fill = '#0072B2') +
  labs(title='Permutation Test Distribution',
       subtitle='Keyword: Trump',
       x = "Cosine Similarity",
       y = 'Count') +
  theme_bw()

ggsave("Analysis/permutation.png", device = "png")
