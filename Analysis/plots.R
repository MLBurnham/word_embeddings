library(dplyr)
library(ggplot2)
setwd("/home/mike/Desktop/Word Embeddings")

# Read in data
# still need to subset to data after date
text <- read.csv('Data/aggregated_tweets.csv')
meta <- read.csv('Meta Data/meta_data.csv')
tweets <- left_join(text, meta, by = 'user_id')
rm(text, meta)

tweets <- tweets[tweets$party == 'R' | tweets$party == 'D',]

ggdata <- count(tweets, party)

# distribution of data by party
ggplot(data=ggdata, aes(x=party, y=n, fill=party)) +
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
ggplot(mpg, aes(cty)) + geom_density(aes(fill=factor(cyl)), alpha=0.8) + 
  labs(title="Density plot", 
       subtitle="City Mileage Grouped by Number of cylinders",
       caption="Source: mpg",
       x="City Mileage",
       fill="# Cylinders")