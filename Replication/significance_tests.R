setwd("/home/mike/Desktop/Word Embeddings")
# libraries
library(perm)
library(dplyr)
library(simpleboot)
library(boot)

##########################
# import  and clean data
##########################

# Cosine similarity data
keysim <- read.csv('Analysis/keyword_similarity.csv')
basesim <- read.csv('Analysis/baseword_similarity.csv')
agreesim <- read.csv('Analysis/agreeword_similarity.csv')

# Relative cosine similarity data
keyrelsim <- read.csv('Analysis/keyword_relative_similarity.csv')
baserelsim <- read.csv('Analysis/baseword_relative_similarity.csv')
agreerelsim <- read.csv('Analysis/agreeword_relative_similarity.csv')

# Cosine similarity Label data    
agreesim$label <- 'Agree'
basesim$label <- 'Base'
keysim$label <- 'Disagree'
cosim <- bind_rows(keysim, agreesim, basesim)

# Relative Cosine similarity Label data    
agreerelsim$label <- 'Agree'
baserelsim$label <- 'Base'
keyrelsim$label <- 'Disagree'
relsim <- bind_rows(keyrelsim, abreerelsim, baserelsim)

##########################
# Significance tests
##########################
# t-tests cosine sim
t.test(keysim$similarity, basesim$similarity)
t.test(keysim$similarity, agreesim$similarity)

# t-tests relative cosine sim
t.test(keyrelsim$similarity, baserelsim$similarity)
t.test(keyrelsim$similarity, agreerelsim$similarity)

# permutation tests agree and disagree words
keyagree <- bind_rows(keysim, agreesim)
permTS(keyagree$similarity ~ keyagree$label, alternative = 'two.sided', method = 'exact.mc')

relkeyagree <- bind_rows(keyrelsim, agreerelsim)
permTS(relkeyagree$similarity ~ relkeyagree$label, alternative = 'two.sided', method = 'exact.mc')

# Permutation tests disagree and base words
keybase <- bind_rows(keysim, basesim)
permTS(keybase$similarity ~ keybase$label, alternative = 'two.sided', method = 'exact.mc')

relkeybase <- bind_rows(keyrelsim, baserelsim)
permTS(keyrelbase$similarity ~ keyrelbase$label, alternative = 'two.sided', method = 'exact.mc')

# Bootstrap disagree words with agree words
agreeboot <- two.boot(keysim$similarity, agreesim$similarity, mean, 1000, na.rm = TRUE)
boot.ci(agreeboot, type = 'perc')

relagreeboot <- two.boot(keyrelsim$similarity, agreerelsim$similarity, mean, 1000, na.rm = TRUE)
boot.ci(relagreeboot, type = 'perc')

# Bootstrap disagree words with base words
baseboot <- two.boot(keysim$similarity, basesim$similarity, mean, 1000, na.rm = TRUE)
boot.ci(baseboot, type = 'perc')

relbaseboot <- two.boot(keyrelsim$similarity, baserelsim$similarity, mean, 1000, na.rm = TRUE)
boot.ci(relbaseboot, type = 'perc')


##########################
# Descriptive Statistics
##########################
mean(agreesim$similarity)
mean(keysim$similarity)
mean(basesim$similarity)
min(basesim$similarity)
min(agreesim$similarity)
min(keysim$similarity)
max(keysim$similarity)
max(agreesim$similarity)
max(basesim$similarity)
length(keysim$similarity)
length(agreesim$similarity)
length(basesim$similarity)
