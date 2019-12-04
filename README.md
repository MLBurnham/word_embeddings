# Measuring ideology via word embeddings
This project is exploring the use of word embeddings to measure ideology.
For my test case I'm using twitter data from US congress members as well as the Russian Troll Tweet Dataset found here: https://github.com/fivethirtyeight/russian-troll-tweets

## To do:
0. Configure environment

    - [x] Init git repo
    - [x] Init remote repo
    - [ ] Set up virtual env
    - [x] Create README.md
    - [ ] Ensure reproducability of scripts
    

1. Get list of all congess members
    - [x] Get keys and access tokens
    - [x] Put keys/tokens in a file
    - [x] Pull cspan list: 


2. scrape meta data for congress members

    - [x] Fields: screen name, user id, about, 
    - [x] Manually add: party, gender, district
    - [ ] Convert meta data notebook to .py script

3. Create listener to stream data
    - [x] Filter for original tweets
    - [x] Test and execute
    - [ ] Stream data to csv
    - [x] Clean up encoding/emoji

4. Create script to request from REST API
    - [x] function to pull the data. Pull max 200 tweets or pull from most recent.
    - [x] function to subset returned tweets to original tweets.
    - [x] function to extract tweets from data and convert to dataframe
    - [x] group functions into class
    - [x] write to csv with twitter id
    - [x] Loop through all members
    - [x] Convert from notebook to modules
    - [ ] Automate daily pull

5. Clean twitter data
    - [x] Merge meta data with text data
    - [x] Convert date strings to datetime and subset to date range
    - [x] Examine lemmas for key political words
    - [x] Remove hashtags
    - [x] Remove websites from text
    - [x] Replace words via regular expressions where appropriate
    - [x] Redefine stopwords
    - [x] Figure out how to handle emoji
    - [x] Tag key words based on ideology affiliation
    - [x] Remove @
    - [ ] Remove single letters
    - [x] Recode PrepDocs class
    
6. Get list of key words
    - [x] Create initial list of 100
    - [x] Revise list based on lemmas
    - [x] Define a dictionary of synonyms for key words
    - [ ] Create list of words where I expect no ideological difference
    - [ ] Add twitter handles for names in synonym list

7. Construct word embeddings
    - [x] Initial word embedding test on 1-2 words
    - [x] Add randomized labels for embeddings
    - [x] PCA and create pca to df function
    - [x] Create plot for pca
    - [x] Test run on 'trump' and 'impeach'
    - [ ] Automate process so I can loop through embeddings for each key word
    - [ ] Find platform to save embeddings on
    - [ ] Congressional word embeddings
    - [ ] Troll word embeddings
    - [x] test skipgram vs cbow

8. Clean troll data
    - [ ] Download data
    - [ ] Clean with same process as congressional data

9. Explore results
    - [ ] Calculate euclidian distance on key terms
    - [ ] Visualize distance via PCA or SVD

10. Test fightnin words process


## Sources:
### Data:
- Congressional meta data: https://github.com/unitedstates/congress-legislators
- CSPAN list of congress memebers on twitter: https://twitter.com/cspan/lists/members-of-congress/members?lang=en
- Russian troll tweets: https://github.com/fivethirtyeight/russian-troll-tweets

### Packages:
- Speed reader package: https://github.com/matthewjdenny/SpeedReader

### Lit:
- Fightin words: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/81B3703230D21620B81EB6E2266C7A66/S1047198700002291a.pdf/div-class-title-fightinandapos-words-lexical-feature-selection-and-evaluation-for-identifying-the-content-of-political-conflict-div.pdf
- word2vec: https://code.google.com/archive/p/word2vec/
- word2vec explained: https://arxiv.org/pdf/1402.3722.pdf
- Diachronic word embeddings: https://arxiv.org/pdf/1605.09096.pdf
- Words are Malleable: https://arxiv.org/pdf/1711.05603.pdf

