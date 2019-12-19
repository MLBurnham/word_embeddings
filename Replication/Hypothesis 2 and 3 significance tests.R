# libraries
library(perm)
library(dplyr)
library(simpleboot)
library(boot)

##########################
# import  and clean data
##########################

sim <- read.csv('Data/word_similarities.csv')
rcs <- select(sim, -similarity)
cs <- select(sim, -relative_similarity)
rm(sim)

######################################
# Significance tests for hypothesis 3
######################################
# t-tests cosine sim
t.test(cs[cs$label == 'disagree',]$similarity, cs[cs$label == 'agree',]$similarity)
t.test(cs[cs$label == 'disagree',]$similarity, cs[cs$label == 'base',]$similarity)

# t-tests relative cosine sim
t.test(rcs[rcs$label == 'disagree',]$relative_similarity, rcs[rcs$label == 'agree',]$relative_similarity)
t.test(rcs[rcs$label == 'disagree',]$relative_similarity, rcs[rcs$label == 'base',]$relative_similarity)

# permutation tests cosine sim
keyagree <- cs[cs$label == 'disagree' | cs$label == 'agree',]
permTS(keyagree$similarity ~ keyagree$label, alternative = 'two.sided', method = 'exact.mc')

keybase <- cs[cs$label == 'disagree' | cs$label == 'base',]
permTS(keybase$similarity ~ keybase$label, alternative = 'two.sided', method = 'exact.mc')

# Permutation tests relative cosine sim
relkeyagree <- rcs[rcs$label == 'disagree' | rcs$label == 'agree',]
permTS(relkeyagree$relative_similarity ~ relkeyagree$label, alternative = 'two.sided', method = 'exact.mc')

relkeybase <- rcs[rcs$label == 'disagree' | rcs$label == 'base',]
permTS(relkeybase$relative_similarity ~ relkeybase$label, alternative = 'two.sided', method = 'exact.mc')

# Bootstrap tests cosine sim
agreeboot <- two.boot(cs[cs$label == 'disagree',]$similarity, cs[cs$label == 'agree',]$similarity, mean, 1000, na.rm = TRUE)
boot.ci(agreeboot, type = 'perc')

baseboot <- two.boot(cs[cs$label == 'disagree',]$similarity, cs[cs$label == 'base',]$similarity, mean, 1000, na.rm = TRUE)
boot.ci(baseboot, type = 'perc')

# Bootstrap tests relative cosine sim
relagreeboot <- two.boot(rcs[rcs$label == 'disagree',]$relative_similarity, rcs[rcs$label == 'agree',]$relative_similarity, mean, 1000, na.rm = TRUE)
boot.ci(relagreeboot, type = 'perc')

relbaseboot <- two.boot(rcs[rcs$label == 'disagree',]$relative_similarity, rcs[rcs$label == 'base',]$relative_similarity, mean, 1000, na.rm = TRUE)
boot.ci(relbaseboot, type = 'perc')

##########################################
# Descriptive Statistics for hypothesis 3
##########################################
# cosine similarity
mean(cs[cs$label == 'agree',]$similarity)
mean(cs[cs$label == 'disagree',]$similarity)
mean(cs[cs$label == 'base',]$similarity)

min(cs[cs$label == 'agree',]$similarity)
min(cs[cs$label == 'disagree',]$similarity)
min(cs[cs$label == 'base',]$similarity)

max(cs[cs$label == 'agree',]$similarity)
max(cs[cs$label == 'disagree',]$similarity)
max(cs[cs$label == 'base',]$similarity)

sd(cs[cs$label == 'agree',]$similarity)
sd(cs[cs$label == 'disagree',]$similarity)
sd(cs[cs$label == 'base',]$similarity)

length(cs[cs$label == 'agree',]$similarity)
length(cs[cs$label == 'disagree',]$similarity)
length(cs[cs$label == 'base',]$similarity)

# Relative cosine similarity
mean(rcs[rcs$label == 'agree',]$relative_similarity)
mean(rcs[rcs$label == 'disagree',]$relative_similarity)
mean(rcs[rcs$label == 'base',]$relative_similarity)

min(rcs[rcs$label == 'agree',]$relative_similarity)
min(rcs[rcs$label == 'disagree',]$relative_similarity)
min(rcs[rcs$label == 'base',]$relative_similarity)

max(rcs[rcs$label == 'agree',]$relative_similarity)
max(rcs[rcs$label == 'disagree',]$relative_similarity)
max(rcs[rcs$label == 'base',]$relative_similarity)

sd(rcs[rcs$label == 'agree',]$relative_similarity)
sd(rcs[rcs$label == 'disagree',]$relative_similarity)
sd(rcs[rcs$label == 'base',]$relative_similarity)

length(rcs[rcs$label == 'agree',]$relative_similarity)
length(rcs[rcs$label == 'disagree',]$relative_similarity)
length(rcs[rcs$label == 'base',]$relative_similarity)

##########################################
# Descriptive Statistics for hypothesis 2
##########################################
mean(placeperm$cosine.similarity)
mean(trumpperm$cosine.similarity)
mean(usmcaperm$cosine.similarity)

min(placeperm$cosine.similarity)
min(trumpperm$cosine.similarity)
min(usmcaperm$cosine.similarity)

max(placeperm$cosine.similarity)
max(trumpperm$cosine.similarity)
max(usmcaperm$cosine.similarity)

sd(placeperm$cosine.similarity)
sd(trumpperm$cosine.similarity)
sd(usmcaperm$cosine.similarity)