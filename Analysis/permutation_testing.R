setwd("/home/mike/Desktop/Word Embeddings")
# libraries
library(perm)
library(dplyr)
library(simpleboot)
library(boot)
# import data
keysim <- read.csv('Analysis/keyword_similarity.csv')
basesim <- read.csv('Analysis/baseword_similarity.csv')
agreesim <- read.csv('Analysis/agreeword_similarity.csv')
agreesim$label <- 'Agree'
basesim$label <- 'Base'
keysim$label <- 'Disagree'
cosim <- bind_rows(keysim, agreesim, basesim)

## t-tests
t.test(keysim$similarity, basesim$similarity)
t.test(keysim$similarity, agreesim$similarity)

## permutation tests
# agree and disagree words
keyagree <- bind_rows(keysim, agreesim)
permTS(keyagree$similarity ~ keyagree$label, alternative = 'two.sided', method = 'exact.mc')
# disagree and base words
keybase <- bind_rows(keysim, basesim)
permTS(keybase$similarity ~ keybase$label, alternative = 'two.sided', method = 'exact.mc')

## Bootstraps
# disagree words with agree words
agreeboot <- two.boot(keysim$similarity, agreesim$similarity, mean, 1000, na.rm = TRUE)
boot.ci(agreeboot, type = 'perc')
# disagree words with base words
baseboot <- two.boot(keysim$similarity, basesim$similarity, mean, 1000, na.rm = TRUE)
boot.ci(baseboot, type = 'perc')