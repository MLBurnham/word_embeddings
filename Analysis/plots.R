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
sim <- read.csv('Data/word_similarities.csv')
rcs <- select(sim, -similarity)
cs <- select(sim, -relative_similarity)

keysim <- read.csv('Analysis/keyword_similarity.csv')
basesim <- read.csv('Analysis/baseword_similarity.csv')
agreesim <- read.csv('Analysis/agreeword_similarity.csv')

# Single word permutation data
trumpperm <- read.csv('Data/trump_permutation.csv')

# generate tweet count table
ggtweets <- count(text, party)

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

ggsave("Results/tweetcount.png", device = "png")

# Density plot of cosine similarity
ggplot(data = cs, aes(similarity)) + geom_density(aes(fill=factor(label)), alpha=0.8) + 
  labs(title="Distribution: Density Plot", 
       subtitle="Cosine Similarity by Category",
       x="Cosine Similarity",
       y="Density",
       fill="Word Category")

ggsave("Results/density.png", device = "png")

# Density plot of relative cosine similarity
ggplot(data = rcs, aes(relative_similarity)) + geom_density(aes(fill=factor(label)), alpha=0.8) + 
  labs(title="Distribution: Density Plot", 
       subtitle="Relative Cosine Similarity by Category",
       x="Cosine Similarity",
       y="Density",
       fill="Word Category")

ggsave("Results/rcs_density.png", device = "png")

# Box plot of cosine similarity
box <- ggplot(data = cs, aes(label, similarity))
box + geom_boxplot() + 
  geom_dotplot(binaxis='y', 
               stackdir='center', 
               dotsize = .5, 
               fill="red") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6)) + 
  labs(title="Distribution: Box Plot", 
       subtitle="Cosine Similarity by Category",
       x="Word Category",
       y="Cosine Similarity") +
  theme_bw()

ggsave("Results/boxplot.png", device = "png")

# Box plot of relative cosine similarity
box <- ggplot(data = rcs, aes(label, relative_similarity))
box + geom_boxplot() + 
  geom_dotplot(binaxis='y', 
               stackdir='center', 
               dotsize = .5, 
               fill="red") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6)) + 
  labs(title="Distribution: Box Plot", 
       subtitle="Relative Cosine Similarity by Category",
       x="Word Category",
       y="Cosine Similarity") +
  theme_bw()

ggsave("Results/rcs_boxplot.png", device = "png")

# Histogram of single word permutation

ggplot(perm, aes(x=cosine.similarity)) + 
  geom_histogram(fill = '#0072B2') +
  labs(title='Permutation Test Distribution',
       subtitle='Keyword: Trump',
       x = "Cosine Similarity",
       y = 'Count') +
  theme_bw()

ggsave("Results/permutation.png", device = "png")
